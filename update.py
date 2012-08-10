#!/usr/bin/python
import os
import sys
import time

	#Build Revision As tmp
print "Downloading revision..."
os.system('cd /usr/share && svn checkout http://subterfuge.googlecode.com/svn/trunk/ subterfuge2')

print "Repopulating..."
	#Removing Old Directory
os.system('mv /usr/share/subterfuge/ /tmp/subterfuge/')
	#Add New Directory
os.system('mv /usr/share/subterfuge2/ /usr/share/subterfuge/')

