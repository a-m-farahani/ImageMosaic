# ImageMosaic
Reconstructing an image by concatenating tiny images or patches. I used images of <a href='https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz'>CIFAR-100</a> as image patches but you can change the ImageTransform function to read images from other sources like your own images.

<b>Example:</b>
<p align="left">
  <img src="https://github.com/a-m-farahani/ImageMosaic/blob/master/images/girl.jpg" height="200" title="Input Image">
  <img src="https://github.com/a-m-farahani/ImageMosaic/blob/master/images/result.jpg" height="200" title="Result Image">
  <img src="https://github.com/a-m-farahani/ImageMosaic/blob/master/images/result_zoom1.jpg" height="200" title="Result Image - Zoomed">
</p>

<b> Usage: </b> <br/>

```python
converter = Image2Mosaic("path to cifar-100 images file", super_pixel_size=(3,3)) <br/>
result = converter.Convert("images/girl.jpg", size=(729,729))
```

<br/>
**Note that size=(h,w), h and w must be divisible by super_pixel_size=(dh,dw). In this example I used size=(729,729) which 729 is divisible by 3.
