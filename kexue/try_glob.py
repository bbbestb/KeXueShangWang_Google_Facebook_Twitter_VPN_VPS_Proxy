import os
import time
import glob


def check_files():
    ''' check files modified in an hour'''
    program_list = ['qemu', 'libvirtd']
    the_dir = '/tmp/'
    time_delta = 3600
    for i in program_list:
        for j in glob.glob('%s/*%s*' % (the_dir, i)):
            if os.path.getmtime(j) >= time.time() - time_delta:
                print 'found file: %s' % j


if __name__ == '__main__':
    check_files()
