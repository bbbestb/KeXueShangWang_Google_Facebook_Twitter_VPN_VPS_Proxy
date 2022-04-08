#!/usr/bin/python
# -*- coding: utf-8 -*-
# 删除1~100的整数中的素数.

import math


def isNotPrime(n):
    flag = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            flag = True
    return flag

for i in filter(isNotPrime, xrange(1, 101)):
    print i
