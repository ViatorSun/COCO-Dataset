# COCO-Dataset
COCO 数据集常用操作

<br>

- json_data_handle: 处理json文件中的 变量
- json_to_dataset : 将标注好的 json 文件转换为 COCO数据集

[原图](https://github.com/ViatorSun/COCO-Dataset/blob/main/HIMG_20211108_144919.jpg)

[原图](https://github.com/ViatorSun/COCO-Dataset/blob/main/HIMG_20211108_144919.png)

<div align="center">
  <img src="HIMG_20211108_144919.jpg#pic_center" width="50%" align=left/><img src="HIMG_20211108_144919.png#pic_center" width="50%" align=right/>
</div>
<br/>

<br>
<br>

将图像复制粘贴至另外文件夹

``` python
path = "./001.jpg"         # 原图片路径
img  = Image.open(path)     # 打开图片

save_path = "../newpath/img.jpg"
img.save("1.jpg")           # 另保存图片
```
