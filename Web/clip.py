# -*- coding:utf-8 -*-

from PIL import Image
import pdb
import numpy as np

'''
 @author:xunalove
  修改文件位置
  修改图片id

'''


def cut():
    # 打开图片图片1.jpg
    name1 = "D:\\OSU\\WebGLVolumeRendering\\Web\\bonsai.raw.png"
    print(name1)
    name2 = "D:\\OSU\\WebGLVolumeRendering\\Web\\bonsai\\clip_"
    im = Image.open(name1)

    # 偏移量
    dx = 256
    dy = 256
    n = 1

    # 左上角切割
    x1 = 0
    y1 = 0
    x2 = dx
    y2 = dy
    print(im.size)  # im.size[0] 宽和高
    w = im.size[0]  # 宽
    h = im.size[1]  # 高

    result = Image.new(im.mode, (w, h))


    # 纵向
    ims = []
    while x2 <= h:
        # 横向切
        while y2 <= w:
            name3 = name2 + str(n) + ".png"
            # print n,x1,y1,x2,y2
            im2 = im.crop((y1, x1, y2, x2))
            # ims.append(im2)
            result.paste(im2, box=(x1,y1))
            # im2.save(name3)
            y1 = y1 + dy
            y2 = y1 + dy
            n = n + 1
        x1 = x1 + dx
        x2 = x1 + dx
        y1 = 0
        y2 = dy
        
    # for i, im in enumerate(ims):
    #     result.paste(im, (0, i*dx))
    result.save('bonsai.png') 
    print("图片切割成功，切割得到的子图片数为")
    return n - 1


if __name__ == "__main__":
    # 切割图片的面积 vx,vy
    # 大
    res = cut()

    print(res)