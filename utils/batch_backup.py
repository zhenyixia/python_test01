# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : 批量备份
# @Time  : 2022/6/18 19:46
import os

from common.sec_constant import back_pwd


def backup_my_document():
    path = r'D:\my-document'
    dst = r'D:\ecloud\我的文档\备份\my-document.rar'

    # C:\softwareinstall\WinRAR\WinRAR.exe a -ep1 -p123  f:\1.rar f:\te
    cmd = f'C:\softwareinstall\WinRAR\WinRAR.exe a -ep1 -p{back_pwd}  {dst} {path}'
    os.system(cmd)
    print('备份成功！')


if __name__ == '__main__':
    # 注： 使用 winrar 备份 与 window自带的任务定时执行程序 实现，不需要自己写脚本了。
    # backup_my_document()
    pass
