from django.conf import settings
settings.configure(DATABASE_ENGINE="sqlite3",
                   DATABASE_HOST="",
                   DATABASE_NAME= os.path.dirname(__file__) + "/db",
                   DATABASE_USER="",
                   DATABASE_PASSWORD="")

from django.db import models
from main.models import *

def attack(method):
    print "Starting Pwn Ops..."
    
    if (method == "auto"):
        print "Running AutoPwn Method..."
        autoconfig()
        (interface, gateway, attackerip, routermac) = getinfo()
        
            #Start Up MITM
        os.system("python " + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + "mitm.py -a &")

        
    else:
        (interface, gateway, attackerip, routermac) = getinfo()



def getinfo():
        #Get Globals from Database
    for settings in setup.objects.all():
        interface     = settings.iface
        gateway       = settings.gateway
        attackerip    = settings.ip
        routermac     = settings.routermac
    
    return interface, gateway, attackerip, routermac



def autoconfig():
          # Read in subterfuge.conf
    with open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r') as file:
        conf = file.readlines()
    
        # Get AutoConfiguration Information
        # Get Interfaces
    f = os.popen("ls /sys/class/net/")
    temp = ''
    temp = f.readline().rstrip('\n')
    result = []
    result.append(temp)
    while (temp != ''):
       temp = f.readline().rstrip('\n')
       if (temp != 'lo'):
                result.append(temp)
    result.remove('')
    
        # Get Gateway
    gw = []
    e = os.popen("route -n | grep 'UG[ \t]' | awk '{print $2}'")
    ttemp = ''
    ttemp = e.readline().rstrip('\n')
    if not ttemp:
       print 'No default gateway present'
    else:
       gw.append(ttemp)
    temp = ''
    gw.append(temp)
    for interface in result:
       f = os.popen("ifconfig " + interface + " | grep \"inet addr\" | sed -e \'s/.*addr://;s/ .*//\'")
       temp2 = ''
       temp3 = ''
       temp = f.readline().rstrip('\n')
       temp2 = re.findall(r'\d*.\d*.\d*.', temp)
       if not temp2:
          print "No default gw on " + interface
       else:
          gate = temp2[0] + '1'
          gw.append(gate)
          result[0] = interface
          autogate = gw[0]
    gw.remove('')
    gw.reverse()
    
        #Read in Config File
    f = open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r')
    conf = f.readlines()
         
        #Get the Local IP Address
    f = os.popen("ifconfig " + result[0] + " | grep \"inet addr\" | sed -e \'s/.*addr://;s/ .*//\'")
    temp2 = ''
    temp3 = ''
    temp = f.readline().rstrip('\n')

    ipaddress = re.findall(r'\d*.\d*.\d*.\d*', temp)[0]
    
        # Edit subterfuge.conf
    print "Using: ", result[0]
    print "Setting gateway as: ", autogate
    conf[17] = autogate + "\n"
    conf[15] = result[0] + "\n"
    conf[26] = ipaddress + "\n"
    
        #Set Database
    setup.objects.update(gateway = autogate)
    setup.objects.update(iface = result[0])
    setup.objects.update(ip = ipaddress) 
    
        # Write to subterfuge.conf
    with open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'w') as file:
        file.writelines(conf)