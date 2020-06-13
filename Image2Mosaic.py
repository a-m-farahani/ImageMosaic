import numpy as np
from scipy.spatial import distance
from PIL import Image
from matplotlib import pyplot as plt

class Image2Mosaic:
  def __init__(self,cifar_path, super_pixel_size=(3,3)):
    self.imgs, self.downsampled_imgs = self.ImageTransform(cifar_path, super_pixel_size)
  
  def unpickle(self,file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict
  
  def DownSampleImage(self, img,reduce=(2,2)):
    h = int(img.shape[0]/reduce[0])
    w = int(img.shape[1]/reduce[1])
    im = np.zeros((reduce[0],reduce[1],3))
    for i in range(reduce[0]):
        hs = i * h
        he = (i+1) * h
        for j in range(reduce[1]):
            ws = j * w
            we = (j+1) * w
            for k in range(3):
                im[i,j,k] = np.mean(img[ hs:he , ws:we , k])
    return im.astype(np.uint8)
  
  def ImageTransform(self, file_path, super_pixel_size):
    f = self.unpickle(file_path)
    images = f[b'data']
    n = images.shape[0]
    images = images.reshape(n,3,32,32).transpose(0,2,3,1)
    
    downsampled_images = np.zeros((n,super_pixel_size[0]*super_pixel_size[1]*3),dtype=np.uint8)
    for i in range(n):
        downsampled_images[i,:] = self.DownSampleImage(images[i,:,:,:],super_pixel_size).flatten()
        print('\rReading Images: {:.2f}%'.format((i+1)/n*100),end='')
    
    print(' --> Done!')
    return (images,downsampled_images)

  def Convert(self, input_image_path, size=(729,729)):
    img = Image.open(input_image_path)
    img = img.resize(size,Image.NEAREST)
    img = np.array(img)
    h,w = img.shape[0],img.shape[1]
    
    res = []
    for i in range(0,h,3):
        t_row = []
        for j in range(0,w,3):
            tmp = img[i:i+3,j:j+3,:].flatten()
            nns = distance.cdist([tmp],self.downsampled_imgs).argmin()
            t_im = self.imgs[nns,:,:,:]
            t_row.append(t_im)
        res.append(np.concatenate(t_row,axis=1))
        print('\Converting...({:.1f}%)'.format((i+1)/h*100),end='')
    print(' --> Completed!')
    
    output = np.concatenate(res,axis=0)
    return output
    
if __name__ == '__main__':
  converter = Image2Mosaic("path_to_cifar_100_image_file", (3,3))
  res = converter.Convert("images/girl.jpg")
  plt.imshow(res)
  plt.show()
