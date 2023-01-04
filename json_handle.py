#  !/usr/bin/env  python
#  -*- coding:utf-8 -*-
# @Time     : 2022.04
# @Author   : 绿色羽毛
# @Email    : lvseyumao@foxmail.com
# @Blog     : https://blog.csdn.net/ViatorSun
# @Paper    : 
# @arXiv    : 
# @version  : "1.0" 
# @Note     : 将标注 img_path 修改成统一格式
# 
#



import argparse
import base64
import json
import os
import os.path as osp

import imgviz
import PIL.Image

from labelme.logger import logger
from labelme import utils


def main(json_File, save_File):
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default = save_File)
    args = parser.parse_args()

    img_name = osp.basename(json_file)[:-5]

    data = json.load(open(json_file))
    imageData = data.get("imageData")
    # imageData = '../images/' + img_name + '.jpg'      # osp.basename(data.get("imageData"))

    # if not imageData:
    img_path = '../images/' + img_name + '.jpg'
    # imagePath = os.path.join(os.path.dirname(json_file), data["imagePath"])
    data["imagePath"] = img_path
    data["imageData"] = None

 
    if not osp.exists(args.out):
        os.makedirs(args.out)

    write_json_data(data, os.path.join(args.out, img_name) + '.json')



def write_json_data(dict, json_path1):
    with open(json_path1, 'w') as r:
        # json.dump(dict, r)
        json.dump(data, r, ensure_ascii=False, indent=2)        # 修改 json内容，保存为 labelme相同格式
    r.close()




if __name__ == "__main__":
    json_path = '/Users/viatorsun/Desktop/Demo/Data/Tomato/TomatoJSON'
    save_path = '/Users/viatorsun/Desktop/Demo/Data/Tomato/NewJson/'
    for root , dirs , files in os.walk(json_path):
        for file in files:
            if file == '.DS_Store':
                continue
            json_path = os.path.join(root ,file)
            print(json_path)
            main(json_path)

