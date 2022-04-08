#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    print 'Hello, %s (in %s)' % (local_school.student,
                                 threading.current_thread().name)


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target= process_thread, args=('Alice',),
                      name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',),
                      name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
