import os
import re
import sys
import time

    #Die Gracefully
def cease():
	print 'Cleaning up...'
	time.sleep(1)
	os.system("kill -9 `ps -A 1 | sed -e '/arpmitm/!d;/sed -e/d;s/^ //;s/ pts.*//'`")
	os.system("kill -9 `ps -A 1 | sed -e '/sslstrip/!d;/sed -e/d;s/^ //;s/ pts.*//'`")
	time.sleep(2)
	f = open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r')
        conf = f.readlines()
	temp = conf[17]
	gateway = temp.rstrip('\n')
        os.system('python ' + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'rearp.py -r ' + gateway + ' &')

