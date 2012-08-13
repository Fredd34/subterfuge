import os
from django.conf import settings
settings.configure(DATABASE_ENGINE="sqlite3",
                   DATABASE_HOST="",
                   DATABASE_NAME="db",
                   DATABASE_USER="",
                   DATABASE_PASSWORD="")

from django.db import models
from main.models import *
from modules.models import *

    #Build Netview Module
print "Configuring Database Space for Modules..."     
print "Building HTTP Code Injection Module"    
newmod = installed(name = "httpcodeinjection")
newmod.save()
print "Building Tunnel Block Module"   
newmod = installed(name = "tunnelblock")
newmod.save()
print "Building Denial of Service Module"   
newmod = installed(name = "dos")
newmod.save()