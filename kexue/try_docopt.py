#!/usr/bin/env python
"""Just try docopt lib for python

Usage:
  try_docopt.py (-h | --help)
  try_docopt.py [options]

Examples:
  try_docopt.py -s +ts5,-ts2 -c +tc5,-tc3

Options:
  -h, --help
  -s, --testsuite suites    #add/remove some testsuites
  -c, --testcase cases      #add/remove some testcases

"""

from docopt import docopt

testsuites = ['ts1', 'ts2', 'ts3', 'ts4']
testcases = ['tc1', 'tc2', 'tc3', 'tc4']


def add_remove(tlist, opt_list):
    '''
    add/remove item in tlist.
    opt_list is a list like ['+ts5', '-ts2'] or ['+tc5', '-tc3'].
    '''
    flag = 0
    for i in opt_list:
        i = i.strip()
        if i.startswith('+'):
            tlist.append(i[1:])
        elif i.startswith('-'):
            if i[1:] in tlist:
                tlist.remove(i[1:])
            else:
                print 'bad argument: %s is not in %s' % (i[1:], tlist)
                flag = 1
        else:
            print 'bad argument: %s' % i
            flag = 1
    if flag:
        return flag
    else:
        return tlist

if __name__ == '__main__':
    args = docopt(__doc__)
    ts_arg = args.get('--testsuite')
    tc_arg = args.get('--testcase')
    if ts_arg:
        ts_opt_list = ts_arg.strip().split(',')
        testsuites = add_remove(testsuites, ts_opt_list)
    if tc_arg:
        tc_opt_list = tc_arg.strip().split(',')
        testcases = add_remove(testcases, tc_opt_list)
    if testsuites != 1 and testcases != 1:
        print 'ts: %s' % testsuites
        print 'tc: %s' % testcases
