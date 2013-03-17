#!/usr/bin/python
import os
import re
import sys
import time
import datetime
import urllib
from django.conf import settings
settings.configure(DATABASE_ENGINE="sqlite3",
                   DATABASE_HOST="",
                   DATABASE_NAME= os.path.dirname(__file__) + "/db",
                   DATABASE_USER="",
                   DATABASE_PASSWORD="")

from django.db import models
from main.models import *


	#Get Globals from Database
for settings in setup.objects.all():
	interface     = settings.iface
	gateway       = settings.gateway


def main():

	print "wtf"
