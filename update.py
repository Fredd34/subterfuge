#!/usr/bin/python
import os
import sys
import time

print "Updating Subterfuge..."
	#Build Revision As tmp
os.system('svn update ' + str(os.path.dirname(__file__)))

