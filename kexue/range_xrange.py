# _*_ coding: utf-8 _*_
'''
Created on Jul 14, 2015

@author: Jay
'''


def my_range(start, end=None, step=1):
    result = []
    if not isinstance(start, int):
        return 'start argument must be an integer.'
    if (not isinstance(end, int)) and (not end is None):
        return 'end argument must be an integer.'
    if not isinstance(step, int):
        return 'step argument must be an integer.'
    elif step == 0:
        return 'step argument must not be zero.'
    if isinstance(end, int):
        while True:
            if start < end:
                result.append(start)
                start += step
            else:
                break
    else:  # end is None
        start, end = 0, start
        while True:
            if start < end:
                result.append(start)
                start += step
            else:
                break
    return result


# 跟range函数的实现基本一样,只是使用yield关键字表示生成器
def my_xrange(start, end=None, step=1):
    if not isinstance(start, int):
        pass
    if (not isinstance(end, int)) and (not end is None):
        pass
    if not isinstance(step, int):
        pass
    elif step == 0:
        pass
    if isinstance(end, int):
        while True:
            if start < end:
                yield start
                start += step
            else:
                break
    else:  # end is None
        start, end = 0, start
        while True:
            if start < end:
                yield start
                start += step
            else:
                break


if __name__ == '__main__':
    print my_range(8)
    print my_range(8, 1, 1)
    print my_range(8, 1.5, 1)
    print my_range(1, 9)
    print my_range(1, 9, 0)
    print [i for i in my_xrange(8)]
    print [i for i in my_xrange(8, 1, 1)]
    print [i for i in my_xrange(8, 1.5, 1)]
    print [i for i in my_xrange(1, 9)]
