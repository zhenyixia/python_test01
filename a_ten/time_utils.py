# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : 时间相关工具
# @Time  : 22/04/03 17:41
import time


def gen_ymd_timestamp():
    """
    生成年月日的时间戳
    :return: 20220403
    """
    return time.strftime("%Y%m%d", time.localtime())
