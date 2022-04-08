# -*- coding: gb2312 -*-

'''
Created on 2013-1-27

@author: Jay Ren
@module: rename_files
@note: rename files in a Windows system.
'''

import os
import re

path = "C:\\Users\\yren9\\Documents\\temp" 

def rename_files():
    prefix = "\[电影天堂-www\.dygod\.com\]"
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file))==True:
            if re.match("\[电影天堂-www\.dygod\.com\].+", file):
                new_name = re.sub(prefix, "", file)
#               print(file)
#               print(new_name)
                os.rename(os.path.join(path,file),os.path.join(path,new_name))

if __name__ == '__main__':
    rename_files()
