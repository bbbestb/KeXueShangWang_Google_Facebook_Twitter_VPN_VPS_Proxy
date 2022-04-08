#!/usr/bin/python2.7
# coding=utf-8

import MySQLdb
import sys

host = 'localhost'
user = 'root'
pwd  = '123456'   # to be modified.
db   = 'test'


if __name__ == '__main__':
    conn = MySQLdb.connect(host, user, pwd, db, charset='utf8');
    try:
        conn.ping()
    except:
        print 'failed to connect MySQL.'
    sql = 'select * from mytable where id = 2'
    cur = conn.cursor()
    cur.execute(sql)
    row = cur.fetchone()
#    print type(row)
    for i in row:
        print i
    cur.close()
    conn.close()
    sys.exit()
