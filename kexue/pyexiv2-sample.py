#!/usr/bin/python2.7
# just a sample for using python-pyexiv2 Library
# pyexiv2 is a Python binding to exiv2, the C++ library for manipulation of EXIF, IPTC and XMP image metadata. 

import pyexiv2
import os

path = '/home/master/Pictures/wall-paper'
for file in os.listdir(path):
	print 'file:' + os.path.join(path,file)
	print '--------------------------------------------------------------'
	metadata = pyexiv2.ImageMetadata(os.path.join(path,file))
	metadata.read()
	print metadata['Exif.Image.DateTime'].value.strftime('%A %d %B %Y, %H:%M:%S')
	print metadata['Exif.Image.ImageDescription'].value
	print metadata['Exif.Image.Software'].value
	print metadata['Exif.Image.ExifTag'].value
	key = 'Exif.Photo.UserComment'
	value = 'A comment.'
	metadata[key] = pyexiv2.ExifTag(key, value)
	# metadata[key] = value    # this a shotcut method as the previous line.
	metadata.write()
	print metadata[key].value
	metadata[key].value ='A new comment.'
	metadata.write()
	print metadata[key].value
	print '--------------------------------------------------------------'
