#!/usr/bin/env python

from __future__ import print_function

import argparse
import glob
import os
import os.path as osp
import sys

import imgviz
import numpy as np

import labelme


def main():
    # parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", default= '/Users/viatorsun/Desktop/Demo/Data/Tomato/TomatoJSON',help="input annotated directory")
    parser.add_argument("--output_dir", default='/Users/viatorsun/Desktop/Demo/Data/Tomato/Instance2' , help="output dataset directory")
    parser.add_argument("--labels", default= '/Users/viatorsun/Desktop/Demo/Data/Tomato/labels.txt', help="labels file") # , required=False
    parser.add_argument("--noviz", default=False, help="no visualization", )  # action="store_true"
    args = parser.parse_args()

    if osp.exists(args.output_dir):
        print("Output directory already exists:", args.output_dir)
        sys.exit(1)
    os.makedirs(args.output_dir)
    os.makedirs(osp.join(args.output_dir, "JPEGImages"))
    os.makedirs(osp.join(args.output_dir, "SegmentClass"))
    os.makedirs(osp.join(args.output_dir, "SegmentClassPNG"))

    if not args.noviz:
        os.makedirs(osp.join(args.output_dir, "SegmentClassVisual") )
    os.makedirs(osp.join(args.output_dir, "SegmentObject"))
    os.makedirs(osp.join(args.output_dir, "SegmentObjectPNG"))

    if not args.noviz:
        os.makedirs(osp.join(args.output_dir, "SegmentObjectVisual") )
    print("Creating dataset:", args.output_dir)

    class_names = []
    class_name_to_id = {}
    for i, line in enumerate(open(args.labels).readlines()):
        class_id = i - 1  # starts with -1
        class_name = line.strip()
        class_name_to_id[class_name] = class_id
        if class_id == -1:
            assert class_name == "__ignore__"
            continue
        elif class_id == 0:
            assert class_name == "_background_"
        class_names.append(class_name)

    class_names = tuple(class_names)
    print("class_names:", class_names)
    out_class_names_file = osp.join(args.output_dir, "class_names.txt")
    with open(out_class_names_file, "w") as f:
        f.writelines("\n".join(class_names))
    print("Saved class_names:", out_class_names_file)

    for filename in glob.glob(osp.join(args.input_dir, "*.json")):
        filename = args.input_dir + '/HIMG_20211109_100940.json'
        print("Generating dataset from:", filename)

        label_file = labelme.LabelFile(filename=filename)

        base = osp.splitext(osp.basename(filename))[0]
        out_img_file = osp.join(args.output_dir, "JPEGImages", base + ".jpg")
        # out_cls_file = osp.join(args.output_dir, "SegmentationClass", base + ".npy")
        out_clsp_file = osp.join(args.output_dir, "SegmentClass", base + ".png")

        if not args.noviz:
            out_clsv_file = osp.join( args.output_dir, "SegmentClassVisual", base + ".jpg",)
        # out_ins_file  = osp.join( args.output_dir, "SegmentationObject", base + ".npy" )
        out_insp_file = osp.join( args.output_dir, "SegmentObject", base + ".png" )

        if not args.noviz:
            out_insv_file = osp.join( args.output_dir, "SegmentObjectVisual", base + ".jpg",)

        img = labelme.utils.img_data_to_arr(label_file.imageData)
        imgviz.io.imsave(out_img_file, img)

        """ cls:语义分割      ins:实例分割 """
        cls, ins = labelme.utils.shapes_to_label(   img_shape=img.shape,
                                                    shapes=label_file.shapes,
                                                    label_name_to_value=class_name_to_id,   )
        ins[cls == -1] = 0  # ignore it.

        # class label       语义分割
        labelme.utils.lblsave(out_clsp_file, cls)
        # np.save(out_cls_file, cls)
        if not args.noviz:
            clsv = imgviz.label2rgb(cls, imgviz.rgb2gray(img), label_names=class_names, font_size=15, loc="rb",   )
            imgviz.io.imsave(out_clsv_file, clsv)

        # instance label    实例
        labelme.utils.lblsave(out_insp_file, ins)
        # np.save(out_ins_file, ins)
        if not args.noviz:
            instance_ids = np.unique(ins)
            instance_names = [str(i) for i in range(max(instance_ids) + 1)]
            insv = imgviz.label2rgb(ins, imgviz.rgb2gray(img), label_names=instance_names, font_size=15, loc="rb"    )
            imgviz.io.imsave(out_insv_file, insv)


if __name__ == "__main__":
    main()
