# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : 斐波那契数列，三种实现
# @Time  : 22/03/16 22:29


import sys


def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    return 1


def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(10):
    print(fibonacci(i), end=" ")

print()


def fibonacci2(n):
    x, y, i = 0, 1, 0
    while i < n:
        print(x, end=" ")
        x, y = y, x + y
        i += 1


fibonacci2(10)
print()


def fibonacci3(n):
    a, b, count = 0, 1, 0
    while True:
        if count == n:
            return
        yield a
        a, b = b, a + b
        count += 1


f = fibonacci3(10)
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
