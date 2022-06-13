# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : 批量修改文件名，同一目录下
# @Time  : 2022/6/13 7:53
import os


def batch_modify(path, to_replaced_str, replaced_str):
    file_names = os.listdir(path)
    for file_name in file_names:
        file_path = os.path.join(path, file_name)
        new_file_name = file_name.replace(to_replaced_str, replaced_str)
        new_file_path = os.path.join(path, new_file_name)
        os.rename(file_path, new_file_path)


if __name__ == '__main__':
    p = r"E:\待整理文件\少儿不宜"
    str1 = ".mp4"
    str2 = ".p4"
    batch_modify(p, str1, str2)
