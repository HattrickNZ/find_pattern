#Description: 
#

#Example of running code 
#


# -*- coding: utf-8 -*-
import os			

dir_path=os.curdir+"/files"	
#files = [f for f in os.listdir('.') if os.path.isfile(f)] # current dir
#files = [f for f in os.listdir(os.curdir ) if os.path.isfile(f)] # current dir
#files = [f for f in os.listdir(dir_path ) if os.path.isfile(os.path.join(dir_path, f))] # print files in dir_path directory
files = [f for f in os.listdir(os.curdir ) if f.endswith(".html")] # list .html files in currdir

print "files of interest: " + str(files)
for f in files:
	# do something
	print dir_path
	print f
	with open(f, 'r') as myfile:
		data=myfile.read().replace('\n', '')
	with open('old', 'r') as myfile:
		search=myfile.read().replace('\n', '')
	print data.count(search)  ## this counts the number of patterns in one file per file
print data.count(search) ## this counts the number of patterns in all the files 