# COCO-Dataset
COCO 数据集常用操作

<br>

- json_data_handle: 处理json文件中的 变量
- json_to_dataset : 将标注好的 json 文件转换为 COCO数据集



<div align="center">
  <img src="Picture/HIMG_20211108_144919.jpg#pic_center" width="40%" align=left/><img src="Picture/HIMG_20211108_144919.png#pic_center" width="40%" align=right/>
</div>


<br>
<br>

将图像复制粘贴至另外文件夹

``` python
path = "./001.jpg"         # 原图片路径
img  = Image.open(path)     # 打开图片

save_path = "../newpath/img.jpg"
img.save(save_path)           # 另保存图片
```

<br>
<br>


修改 labelme 标注好的JSON文件，并依旧保存为 labelme格式
```python
with open(json_path, 'w') as r:
      json.dump(data, r, ensure_ascii=False, indent=2)
r.close()
```
