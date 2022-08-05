# 流程记录

## 数据增强



- 宽度和高度偏移  

    >  ```python
    >  generator = tf.keras.preprocessing.image.ImageDataGenerator(width_shift_range=[-90,-40,0,40,90],height_shift_range=[-40,0,40])
    >  x, y = next(generator.flow_from_directory('images', batch_size=1))
    >  plt.imshow(x[0].astype('uint8'));
    >  ```

- 亮度  
    > ```python
    > generator = tf.keras.preprocessing.image.> ImageDataGenerator(brightness_range=(0.8,4.2))
    > x, y = next(generator.flow_from_directory> ('images', batch_size=1))
    > plt.imshow(x[0].astype('uint8'));
    > ```

- 剪切变换
    > ```python  
    > generator = tf.keras.preprocessing.image.> ImageDataGenerator(shear_range=46)
    > x, y = next(generator.flow_from_directory> ('images', batch_size=1))
    > plt.imshow(x[0].astype('uint8'));
    > ```
- 频道转换
    > ```python
    > generator = tf.keras.preprocessing.image.ImageDataGenerator(channel_shift_range=180   )
    > x, y = next(generator.flow_from_directory('images', batch_size=1))
    > plt.imshow(x[0].astype('uint8'));
    > ```
- 翻转
    >```python  
    >generator = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True,vertical_flip=True)  
    >x, y = next(generator.flow_from_directory('images', batch_size=1))  
    >plt.imshow(x[0].astype('uint8'));
    >```
