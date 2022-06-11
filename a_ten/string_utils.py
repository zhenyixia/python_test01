# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : 字符串工具
# @Time  : 22/04/03 17:41


# 匹配 所有字母
import re

re_letters = re.compile(r'([a-zA-Z]+)')


def count_word_num(string):
    """
    统计字符串中字母的个数
    :param string: "abc我中国cdf，abc人”
    :return:  3
    """
    matches = re.findall(re_letters, string)
    if not matches:
        return 0
    else:
        return len(matches)