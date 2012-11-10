import os
import re
import sys
import time
from subterfuge.main.models import *

    #Die Gracefully
def cease():
	print 'Cleaning up...'
	time.sleep(1)
	os.system("kill -9 `ps -A 1 | sed -e '/arpmitm/!d;/sed -e/d;s/^ //;s/ pts.*//'`")
	os.system("kill -9 `ps -A 1 | sed -e '/arpwatch/!d;/sed -e/d;s/^ //;s/ pts.*//'`")
	os.system("kill -9 `ps -A 1 | sed -e '/sslstrip/!d;/sed -e/d;s/^ //;s/ pts.*//'`")
	time.sleep(1)
	
		#Get Globals from Database
	for settings in setup.objects.all():
		interface     = settings.iface
		gateway       = settings.gateway
		attackerip    = settings.ip
		routermac     = settings.routermac
		smartarp      = settings.smartarp
	
		#ReARP The Network
	os.system('python ' + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'utilities/rearp.py -r ' + gateway + ' &')

