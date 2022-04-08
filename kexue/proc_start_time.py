'''
get the start time of a process
e.g. python proc_start_time.py -p 12345
'''
import argparse
import psutil
import os
import time


def get_start_time(pid):
    ''' return the start time in human readable string '''
    p = psutil.Process(int(pid))
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(p.create_time()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pid", help="PID of a process")
    args = parser.parse_args()
    if not args.pid:
        args.pid = os.getpid()
    print get_start_time(args.pid)
