#! /usr/bin/python3
# coding=utf-8

'''
Created on Nov 9, 2011

@author: Jay Ren
@note: get some stock prices.  need to know how to deal with some numbers and print formate.
'''

import urllib.request

def get_price(code):
	url = 'http://hq.sinajs.cn/?list=%s' % code
	req = urllib.request.Request(url)
	req.set_proxy('proxy01.XXXX.com:8080', 'http')
	content = urllib.request.urlopen(req).read()
	#print(content)
	str = content.decode('gbk')
	#print(content)
	#print(str)
	data = str.split('"')[1].split(',')
	name = "%-6s" % data[0]
	price_current = "%-6s" % float(data[3])
	change_percent = ( float(data[3]) - float(data[2]) )*100 / float(data[2])
	change_percent = "%s%%" % round(change_percent, 2)
	change_percent = "%-6s" % change_percent
	print("股票名称:{0} 涨跌幅:{1} 最新价:{2}".format(name, change_percent, price_current) )

def get_all_price(code_list):
	for code in code_list:
		get_price(code)

def get_index(code):
	url = 'http://hq.sinajs.cn/?list=%s' % code
	req = urllib.request.Request(url)
	req.set_proxy('proxy01.XXXX.com:8080', 'http')
	content = urllib.request.urlopen(req).read()
	#print(content)
	str = content.decode('gbk')
	#print(content)
	#print(str)
	data = str.split('"')[1].split(',')
	name = "%-6s" % data[0]
	price_current = "%-6s" % float(data[3])
	change_percent = ( float(data[3]) - float(data[2]) )*100 / float(data[2])
	change_percent = "%-6s" % ("%s%%" % round(change_percent, 2))
	print("指数名称:{0} 涨跌幅:{1} 最新指数:{2}".format(name, change_percent, price_current) )

def get_all_index(index_code_list):
	for code in index_code_list:
		get_index(code)

code_list = ['sz300036', 'sz000977', 'sh600718', 'sh600489']
get_all_price(code_list)
print("-----------------------------------------------------------------")
index_code_list = ['sh000001', 'sz399001']
get_all_index(index_code_list)
