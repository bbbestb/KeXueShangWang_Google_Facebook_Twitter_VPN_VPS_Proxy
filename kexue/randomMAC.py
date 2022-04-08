#!/usr/bin/python
# *-* coding:utf-8 *-*

import random


def randomMAC():
    '''
    generate random MAC address.
    the first 24 bits are for OUI (Organizationally Unique Identifier).
    OUI是由IEEE的注册管理机构给不同厂家分配的代码，区分了不同的厂家。
    '''
    mac = [0x00, 0x8c, 0xfa,
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)
           ]
    return ':'.join(map(lambda x: "%02x" % x, mac))


if __name__ == '__main__':
    print randomMAC()
