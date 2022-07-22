# COCO-Dataset
COCO 数据集常用操作

<br>

- json_data_handle: 处理json文件中的 变量


<br>
<br>

将图像复制粘贴至另外文件夹

``` python
path = "./001.jpg"         # 原图片路径
img  = Image.open(path)     # 打开图片

save_path = "../newpath/img.jpg"
img.save("1.jpg")           # 另保存图片
```
