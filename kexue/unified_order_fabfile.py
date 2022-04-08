#!/usr/bin/env python
# a fabfile to manange the performance test for unified order project.
# usage: fab -f unified_order_fabfile.py start_jmeter -P -z 30
# author: Jay <smile665@gmail.com>

from fabric.context_managers import cd
from fabric.operations import run, put
from fabric.api import task, env

env.hosts = ['192.168.1.2', '192.168.1.3', '192.168.1.4']
env.port = 22
env.user = 'root'
env.password = '123456'


@task
def hostname():
    # show hostname   # just for testing
    with cd('/tmp'):
        run('hostname')


@task
def copy_jmeter():
    # copy jmeter to other machines
    with cd('/tmp'):
        run('rm -rf jakarta-jmeter-2.3.4')
        put('jakarta-jmeter-2.3.4', '/tmp/')
        run('cd jakarta-jmeter-2.3.4/bin; chmod a+x jmeter')
        #run('ls /tmp/')


@task
def start_jmeter():
    # run jmeter in all test clients
    #with cd('/tmp/'):
    with cd('/tmp/jakarta-jmeter-2.3.4/bin/'):
        run('screen -d -m ./jmeter -n -t my-order.jmx -l log.jtl &>abc.log')
        #run('./jmeter -n -t unified-order.jmx -l log.jtl &>abc.log')
        #run('screen -d -m sleep 10', pty=False)
        #run('service tomcat start', pty=False)


@task
def kill_jmeter():
    # kill the jmeter processes for unified order project
    with cd('/tmp/'):
        pids = run("ps -ef | grep unified | grep -v 'grep' | awk '{print $2'}")
        pid_list = pids.split('\r\n')
        for i in pid_list:
            run('kill -9 %s' % i)


@task
def get_status():
    # get jmeter(java) running status
    with cd('/tmp'):
        run('ps -ef | grep unified | grep java | grep -v grep')
