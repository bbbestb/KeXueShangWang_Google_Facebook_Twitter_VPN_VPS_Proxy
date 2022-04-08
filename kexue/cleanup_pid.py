#!/usr/bin/env python

import os
import subprocess

base_dir = '/tmp/pid_dir'
pid_files = ['ut.pid', 'ft.pid']
max_seconds = 48 * 3600


def check_pid(pid):
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


def get_elapsed_time(pid):
    '''get the elapsed time of the process with this pid'''
    cmd = 'ps -p %s -o pid,etime' % str(pid)
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    # get data from stdout
    proc.wait()
    results = proc.stdout.readlines()
    # parse data (should only be one)
    for result in results:
        try:
            result.strip()
            if result.split()[0] == str(pid):
                pidInfo = result.split()[1]
                # stop after the first one we find
                break
        except IndexError:
            pass    # ignore it
    else:
        # didn't find one
        print "Process PID %s doesn't seem to exist!" % pid
        return 0
    pidInfo = [result.split()[1] for result in results
               if result.split()[0] == str(pid)][0]
    pidInfo = pidInfo.partition("-")
    if pidInfo[1] == '-':
        # there is a day
        days = int(pidInfo[0])
        rest = pidInfo[2].split(":")
        hours = int(rest[0])
        minutes = int(rest[1])
        seconds = int(rest[2])
    else:
        days = 0
        rest = pidInfo[0].split(":")
        if len(rest) == 3:
            hours = int(rest[0])
            minutes = int(rest[1])
            seconds = int(rest[2])
        elif len(rest) == 2:
            hours = 0
            minutes = int(rest[0])
            seconds = int(rest[1])
        else:
            hours = 0
            minutes = 0
            seconds = int(rest[0])

    elapsed_time = days*24*3600 + hours*3600 + minutes*60 + seconds
    return elapsed_time


def remove_pid(pidfiles):
    '''remove pid files if the process is not running.'''
    for i in pidfiles:
        filepath = '%s/%s' % (base_dir, i)
        if os.path.exists(filepath):
            del_flag = 0
            with open(filepath) as f:
                pid = f.read()
                if not check_pid(int(pid)):
                    print 'pid file: %s' % i
                    print 'process does not exist with pid %s' % pid
                    del_flag = 1
                elif get_elapsed_time(pid) > max_seconds:
                    print 'elapsed_time is greater than max_seconds'
                    print 'tring to kill pid %s' % pid
                    os.kill(int(pid), 9)
                    del_flag = 1
            if del_flag:
                os.unlink(filepath)


if __name__ == '__main__':
    remove_pid(pid_files)
