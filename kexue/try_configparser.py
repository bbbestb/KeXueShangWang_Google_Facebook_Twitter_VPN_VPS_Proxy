#!/usr/bin/env python

import ConfigParser

config = ConfigParser.ConfigParser()
config.read('my.cfg')

print config.get('mysqld', 'socket')
print config.get('mysqld_safe', 'pid-file')
print config.get('jay_test', 'greeting', raw=0)
print config.get('jay_test', 'greeting', raw=1)

config.set('jay_test', 'log', '/var/log/jay-test-new.log')
config.add_section('new_section')
config.set('new_section', 'language', 'Python')
with open('my-new.cfg', 'wb') as configfile:
        config.write(configfile)
