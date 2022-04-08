#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2016, Jay <smile665@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import syslog
import subprocess
import time

DOCUMENTATION = '''
---
module: rpmdb
short_description: Manages the rpm database.
description:
  - Check and rebuild the rpm database.
version_added: "2.0"
options:
  action:
    choices: [ "check", "rebuild" ]
    description:
      - The action name.
      - check: only check if rpm db is OK or not.
      - rebuild: rebuild rpm db if it is NOT OK.
    required: false
    default: check
  timeout:
    description:
      - The TIMEOUT seconds when checking rpm db.
    required: false
    default: 10
notes: []
requirements: [ rpm, rm ]
author: Jay <smile665@gmail.com>
'''

EXAMPLES = '''
- rpmdb: action=check
- rpmdb: action=rebuild
'''

# ==============================================================


RPMBIN = '/bin/rpm'


def log(msg):
    syslog.openlog('ansible-%s' % os.path.basename(__file__))
    syslog.syslog(syslog.LOG_NOTICE, msg)


def execute_command(module, cmd):
    log('Command %s' % '|'.join(cmd))
    return module.run_command(cmd)


def check_db(module, timeout=10):
    rc = 0
    logfile = '/tmp/rpm-qa.log'
    elapsed_time = 0
    cmd = '%s -qa &> %s' % (RPMBIN, logfile)
    child = subprocess.Popen(cmd, shell=True)
    
    while elapsed_time <= timeout:
        child_ret = child.poll()
        if child_ret is None:  # child still running
            time.sleep(1)
            elapsed_time += 1
        elif child_ret == 0:
            if 'error:' in open(logfile, 'r').read():
                rc = 1
                break
            else:  # cmd is excuted with no error.
                break
        else:
            rc = 2
            break
    if elapsed_time > timeout:
        child.kill()
        time.sleep(1)
        rc = 3
    return rc


def rebuild_db(module):
    rmdb_cmd = ['rm', '-f', '/var/lib/rpm/__db.*']
    rc1, out1, err1 = execute_command(module, rmdb_cmd)
    cmd = [RPMBIN, '--rebuilddb']
    rc, out, err = execute_command(module, cmd)
    return (rc == 0) and (rc1 == 0)


# main
def main():

    # defining module
    module = AnsibleModule(
        argument_spec=dict(
            action = dict(required=False, default='check', choices=['check', 'rebuild']),
            timeout = dict(required=False, default=10, type='int')
        )
    )

    changed = False
    msg = ''
    action = module.params['action']
    timeout = module.params['timeout']
    check_cmd = 'rpm -qa'

    if action == 'check':
        rc = check_db(module, timeout)
        if rc == 1:
            module.fail_json(msg='Error when running cmd: %s' % (check_cmd))
        elif rc == 2:
            module.fail_json(msg='return code error. cmd: %s' % (check_cmd))
        elif rc == 3:
            module.fail_json(msg='Timeout %d s. cmd: %s'      % (timeout, check_cmd))
        elif rc == 0:
            msg = 'OK. cmd: %s' % check_cmd
            
    elif action == 'rebuild':
        rc = check_db(module, timeout)
        if rc != 0:
            if rebuild_db(module):
                changed = True
                msg = 'OK. rm -f /var/lib/rpm/__db.00*; rpm --rebuilddb'
            else:
                msg = 'Error. rm -f /var/lib/rpm/__db.00*; rpm --rebuilddb'
                module.fail_json(msg=msg)

    module.exit_json(
        changed = changed,
        action = action,
        msg = msg
    )

# this is magic, see lib/ansible/executor/module_common.py
#<<INCLUDE_ANSIBLE_MODULE_COMMON>>
main()
