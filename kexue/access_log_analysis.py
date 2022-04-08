'''
Created on Oct 20, 2013
@summary: to analyze apache access_log and list the top N IPs of the visitors.
          for my website, I found many spam visitors.
@author: Jay <smilejay.com>
'''
import resource
import time
import glob
from itertools import groupby
from operator import itemgetter
from heapq import nlargest
from iplocation import location_taobao, location_qq, location_freegeoip

# the sample dirctory is on a Mac OS X system.
log_dir = '/Users/jay/workspace/python_study/data/httpd'
default_file = '/Users/jay/workspace/python_study/data/httpd/access_log'

def get_top_n_ip(log_file=default_file, top_n=20):
    """ list the top n IPs in a access_log file
    
    return the list of tuples ('110.84.0.129', 9999), by default it returns top 20
    """
    
    ip_list = []
    with open(log_file) as access_log:
        for line in access_log:
            cols = [x for x in line.split()]
            ip_list.append(cols[0])
            
#        print 'RAM used: %d MB' % int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024/1024)
#        time.sleep(3)
        ip_list.sort(cmp=None, key=None, reverse=False)
        ip_dict = {}
#        print [len(list(group)) for key, group in groupby(ip_list)]
        for key, value in groupby(ip_list):
            ip_dict[key] = len(list(value))
##        sorted_dict = sorted(ip_dict.iteritems(), key=itemgetter(1), reverse=True)[:top_n]
#        print sorted_dict
#        print nlargest(top_n, ip_dict.iteritems(), itemgetter(1))
        return nlargest(top_n, ip_dict.iteritems(), itemgetter(1))

def get_access_logs(file_dir=log_dir):
    """ list the access_log files in the a directory
    
    return a list of the files with absolute path.
    """
    
    file_list = []
    for myfile in glob.glob1(file_dir, 'access_log*'):
        file_list.append('%s/%s' % (file_dir, myfile))
#    print file_list
    return file_list

def remove_localhost_ip(ip_dict):
    """ remove localhost ('::1') from the ip_dict
    
    """
    localhost_key = '::1'
    ip_dict.pop(localhost_key)
    return ip_dict

def merge_top_n_ips(file_dir=log_dir, top_n=50):
    """ merge the top n IPs in all of the files in the file_dir 
    
    for a IP, it will add all the existing counts together.
    After merging, 
    return the list of tuples ('110.84.0.129', 19999), by default it returns top 50
    """
    
    top_ip_list = []
    ip_list = []
    top_ip_dict = {}
    file_list = get_access_logs(file_dir)
    for i in range(len(file_list)):
        top_20_ip_list = get_top_n_ip(file_list[i], 20)
        for j in top_20_ip_list:
            ip_list.append(j[0])
        top_ip_list.append(top_20_ip_list)
    
    uniq_ip_list = list(set(ip_list))
    for ip in uniq_ip_list:
        top_ip_dict[ip] = 0

    for ip in list(uniq_ip_list):
        for i in top_ip_list:
            for j in i:
                if j[0] == ip:
                    top_ip_dict[ip] += j[1]
    remove_localhost_ip(top_ip_dict)
#    print top_ip_dict
#    print nlargest(top_n, top_ip_dict.iteritems(), itemgetter(1))
    return nlargest(top_n, top_ip_dict.iteritems(), itemgetter(1))

def get_top_ip_prefix(top_ip_list):
    """ list the first 2 sections (prefix) of the the IP list
    
        list the IPs with the same prefix; we should pay more attention to these ip prefix
    """
    prefix_list = []
    prefix_pv_list = []
    prefix_pv_count_list = []
    for i in top_ip_list:
        num_list = i[0].split('.')
        prefix = '%s.%s' % (num_list[0], num_list[1])
        prefix_list.append(prefix)
        prefix_pv_list.append((prefix, i[1]))
    uniq_prefix_list = list(set(prefix_list))
    for prefix in uniq_prefix_list:
        tmp_list = []
        tmp_pv = 0
        tmp_list.append(prefix)
        for j in prefix_pv_list:
            if j[0] == prefix:
                tmp_pv += j[1]
        tmp_list.append(tmp_pv)
        tmp_list.append(prefix_list.count(prefix))
        prefix_pv_count_list.append(tmp_list)
    
    return sorted(prefix_pv_count_list, key=itemgetter(1), reverse=True)
    
def show_top_n_ip_geo():
    top_ip_list = merge_top_n_ips(log_dir)
    ipprefix_pv_count_list = get_top_ip_prefix(top_ip_list)
    print('-----------top 50 ip and its pv -----------')
    for i in top_ip_list:
        geoinfo = location_taobao(i[0]).get_region()
        print('%s  %s  %s' % (i[0], geoinfo, i[1]))
    print('')
    print('---------- top ip-prefix and its pv --------')
    for j in ipprefix_pv_count_list:
        geoinfo = location_taobao('%s.0.0' % j[0]).get_region()
        print('%s %s %s %d' % (j[0], geoinfo, j[1], j[2]))

if __name__ == '__main__':
#    get_top_20_ip()
#    get_access_logs()
#    merge_top_n_ips(log_dir, 50)
    top_ip_list = [('110.84.0.129', 118926), ('175.44.13.57', 30833), ('175.44.55.67', 30532), \
                   ('175.44.32.161', 30455), ('112.111.184.64', 30206), ('218.6.2.177', 24958), \
                   ('117.26.255.120', 24310), ('220.161.103.41', 23361), ('112.111.172.250', 23009), \
                   ('175.44.8.176', 22990), ('27.153.128.68', 19397), ('59.58.138.190', 18834), \
                   ('59.58.138.184', 17083), ('220.161.103.87', 16560), ('120.33.241.180', 16035), \
                   ('175.44.13.183', 15905), ('220.161.103.211', 15516), ('117.26.73.89', 14370), \
                   ('58.22.74.52', 12634), ('175.44.14.172', 12275), ('175.44.19.36', 11490), \
                   ('112.111.183.215', 10790), ('175.42.94.30', 10518), ('36.248.160.186', 9962), \
                   ('175.42.95.186', 9696), ('112.111.187.190', 9688), ('175.42.94.90', 9314)]
#    print len(top_ip_list)
#    get_top_ip_prefix(top_ip_list)
    show_top_n_ip_geo()