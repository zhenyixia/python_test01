# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : 删除空文件夹
# @Time  : 2022/6/13 12:50
import os


def remove_empty_dirs(path):
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)

            if not os.listdir(dir_path):
                print(f"Begin to delete dir: {dir_path}.")
                os.rmdir(dir_path)



if __name__ == '__main__':
    p = r'D:\天翼云盘下载'
    remove_empty_dirs(p)