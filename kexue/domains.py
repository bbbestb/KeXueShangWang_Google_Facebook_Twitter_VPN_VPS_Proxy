#!/usr/bin/env python
import time
import libvirt


def destroy_domains():
    '''
    destroy all domains() via libvirt python API.
    '''
    conn = libvirt.open(None)
    if conn:
        for i in conn.listDomainsID():
            dom = conn.lookupByID(i)
            dom.destroy()
            time.sleep(1)
        if conn.listDomainsID():
            print 'ERROR! there are live domains.'
    else:
        print 'Failed to open connection to the hypervisor'


if __name__ == '__main__':
    destroy_domains()
