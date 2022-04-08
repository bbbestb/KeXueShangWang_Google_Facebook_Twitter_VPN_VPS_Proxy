#!/usr/bin/env python


def task(num):
    ret = []
    if num < 1:
        return None
    elif num == 1:
        ret = [1]
    else:
        ret_before = task(num - 1)
        for i in (xrange(num)):
            if i == 0:
                ret.append(1)
            elif len(ret_before) <= i:
                ret.append(ret_before[i - 1])
            else:
                ret.append(ret_before[i - 1] + ret_before[i])
    return ret


for i in range(6):
    if task(i):
        print task(i)
