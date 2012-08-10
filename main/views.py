import os
    #Django Web Modules
from django.template import Context, loader
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.template import RequestContext
    #Database Models
from subterfuge.main.models import credentials
from subterfuge.modules.models import *
    #Additional Views
from subterfuge.cease.views import *
from subterfuge.modules.views import *

@csrf_protect
@never_cache
def index(request):
   if request.is_ajax():
	      #Get Creds from DB
      creds = credentials.objects.all()

         #Reset Injection Counter
      iptrack.objects.update(injected = "0")

	      #Check Arpspoof status
      command = "ps -A 1 | sed -e '/arpmitm/!d;/sed -e/d;s/^ //;s/ pts.*//'"
      a = os.popen(command)
      reply = a.read()
      if(len(reply)>1):
	      status = "on"
      else:
	      status = "off"
	
         
	      #Relay Template Variables
      return render_to_response("includes/credtable.inc", {
	      "credential"    :   creds,
	      "status"	      :	  status,
      })
   else:            
	      #Check Arpspoof status
      command = "ps -A 1 | sed -e '/arpmitm/!d;/sed -e/d;s/^ //;s/ pts.*//'"
      a = os.popen(command)
      reply = a.read()
      if(len(reply)>1):
	      status = "on"
      else:
	      status = "off"

	
	      # Read in subterfuge.conf
      with open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r') as file:
         conf = file.readlines()
         
	      #Relay Template Variables
      return render_to_response("home.ext", {
	      "status"    :   status,
	      "conf"      :   str(conf[20]).rstrip('\n'),
      })
        
        
def plugins(request):
    if request.is_ajax():
        print "AJAX REQUEST!"
    else:
      		#Read in Config File
        f = open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r')
        config = f.readlines()
        
        modules = installed.objects.all()
                   
            #Relay Template Variables
        return render_to_response("plugins.ext", {
            "config"    :   config,
            "modules"   :   modules,
        })

def hostcheck(request):
    if request.is_ajax():
      		#Read in Config File
        f = open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r')
        config = f.readlines()
        
        		#Check ARP Poison status
        command = "ps -A 1 | sed -e '/arpmitm/!d;/sed -e/d;s/^ //;s/ pts.*//'"
        a = os.popen(command)
        reply = a.read()
        if(len(reply)>1):
        	status = "on"
        else:
        	status = "off"
        
        modules = installed.objects.all()
        client  = iptrack.objects.exclude(id = "1").all()
        scanout = scan.objects.all()
        
           #Relay Template Variables
        return render_to_response("includes/hostcheck.inc", {
            "config"    :   config,
            "modules"   :   modules,
            "client"    :   client,
            "scan"      :   scanout,
            "status"	:   status,
        })        
        
def netview(request):
    if request.is_ajax():
      		#Read in Config File
        f = open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r')
        config = f.readlines()
        
        		#Check ARP Poison status
        command = "ps -A 1 | sed -e '/arpmitm/!d;/sed -e/d;s/^ //;s/ pts.*//'"
        a = os.popen(command)
        reply = a.read()
        if(len(reply)>1):
        	status = "on"
        else:
        	status = "off"
        
        modules = installed.objects.all()
        client  = iptrack.objects.exclude(id = "1").all()
        scanout = scan.objects.all()
        
           #Relay Template Variables
        return render_to_response("includes/netview.inc", {
            "config"    :   config,
            "modules"   :   modules,
            "client"    :   client,
            "scan"      :   scanout,
            "status"	:   status,
        })
        
    else:
      		#Read in Config File
        f = open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r')
        config = f.readlines()
        
        '''
        newmod = installed(name = "httpcodeinjection")
        newmod.save()
        newmod = installed(name = "tunnelblock")
        newmod.save()
        newmod = installed(name = "dos")
        newmod.save()
         '''       

		       #Check ARP Poison status
        command = "ps -A 1 | sed -e '/arpmitm/!d;/sed -e/d;s/^ //;s/ pts.*//'"
        a = os.popen(command)
        reply = a.read()
        if(len(reply)>1):
        	status = "on"
        else:
        	status = "off"
        
        modules = installed.objects.all()
        client  = iptrack.objects.exclude(id = "1").all()
        scanout = scan.objects.all()
        
           #Relay Template Variables
        return render_to_response("netview.ext", {
            "config"    :   config,
            "modules"   :   modules,
            "client"    :   client,
            "scan"      :   scanout,
            "status"		:	 status,
        }) 
        

def netctrl(request, cmd):
    if request.is_ajax():

        if cmd == "scan":
            address = request.POST["target"]
            os.system("python " + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + "scan.py " + address + " &")

        if cmd == "expand":
            iptrack.objects.filter(address = request.POST["address"]).update(expand = "1")

        if cmd == "shrink":
            iptrack.objects.filter(address = request.POST["address"]).update(expand = "0")

      		#Read in Config File
        f = open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r')
        config = f.readlines()
        
        
        modules = installed.objects.all()
        client  = iptrack.objects.exclude(id = "1").all()
        scanout = scan.objects.all()
        
           #Relay Template Variables
        return render_to_response("mods/netview.mod", {
            "config"    :   config,
            "modules"   :   modules,
            "client"    :   client,
            "scan"      :   scanout,
        }) 
        
    else:
                   
            #Relay Template Variables
        return render_to_response("netview.ext", {
            "config"    :   "um",
        })    
        
        
        
        #Writes to the Config File are handled here
def conf(request, module):
      # Read in subterfuge.conf
   with open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r') as file:
      conf = file.readlines()

      # Subterfuge Settings Configuration
      # Edit subterfuge.conf
   if module == "settings":
      try:
         conf[15] = request.POST["iface"] + "\n"
         print "Using Interface => " + request.POST["iface"]
      except:
         print "Interface Not Found... Skipping"
         
      if request.POST["auto"] == "yes":
         conf[20] = "yes" + "\n"
      else:
         conf[20] = "no" + "\n"
         
      try:
         conf[17] = request.POST["agw"] + "\n"
         print "Using Gateway   => " + request.POST["agw"]
      except:
         print "Automatic Gateway was not selected"
         
      try:
         conf[17] = request.POST["mgw"] + "\n"
         print "Using Gateway   => " + request.POST["mgw"]
      except:
         print "Manual Gateway was not selected"
         
         #Get the Local IP Address
      '''
      f = os.popen("ifconfig " + conf[15] + " | grep \"inet addr\" | sed -e \'s/.*addr://;s/ .*//\'")
      temp2 = ''
      temp3 = ''
      temp = f.readline().rstrip('\n')

      ipaddress = re.findall(r'\d*.\d*.\d*.\d*', temp)[0]
      conf[26] = ipaddress + "\n"
      '''

   if module == "update":
      print 'python ' + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'update.py'
      os.system('python ' + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'update.py')

      #################################
      #Subterfuge Module Configurations
      #################################
      
   if module == "httpinjection":   
      httpcodeinjection(request, conf)
      
   elif module == "tunnelblock":   
      tunnelblock()
      
   else:
      for mod in installed.objects.all():
         if module == mod.name:
           os.system('python ' + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'modules/' + module + '/' + module + '.py &')
   
              
      #################################
      #  END MODULE CONFIGURATION
      #################################
   
      # Write to subterfuge.conf
   with open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'w') as file:
      file.writelines(conf)
      
      
      # Call Index Page
	   # Check Arpspoof status
   command = "ps -A 1 | sed -e '/arpmitm/!d;/sed -e/d;s/^ //;s/ pts.*//'"
   a = os.popen(command)
   reply = a.read()
   if(len(reply)>1):
	   status = "on"
   else:
	   status = "off"
	   #Relay Template Variables
   return render_to_response(request.META['HTTP_REFERER'].split('/')[3] + ".ext", {
	   "status"    :   status,
   })
        
def settings(request):
    if request.is_ajax():
        print "AJAX REQUEST!"

    else:            
	      #Get Interfaces
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
        
         #Get Gateway
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
              gw.remove('')
              gw.reverse()
              
        		#Read in Config File
      f = open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r')
      config = f.readlines()
        
     
           	#Check Arpspoof status
      command = "ps -A 1 | sed -e '/arpmitm/!d;/sed -e/d;s/^ //;s/ pts.*//'"
      a = os.popen(command)
      reply = a.read()
      if(len(reply)>1):
            status = "on"
      else:
            status = "off"
           
           
            #Relay Template Variables
      return render_to_response("settings.ext", {
            "config"    :   config,
            "conf"      :   str(config[20]).rstrip('\n'),
            "iface"	:   result,
            "gateway"   :   gw,
            "status"    :   status,
         })

  
        #Command Definitions:
def startpwn(request, method):
    if request.is_ajax():
      if (method == "auto"):
        print "Running AutoPwn Method..."
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
        
            # Edit subterfuge.conf
        print "Using: ", result[0]
        print "Setting gateway as: ", autogate
        conf[17] = autogate + "\n"
        conf[15] = result[0] + "\n"
             
            #Get the Local IP Address
        f = os.popen("ifconfig " + result[0] + " | grep \"inet addr\" | sed -e \'s/.*addr://;s/ .*//\'")
        temp2 = ''
        temp3 = ''
        temp = f.readline().rstrip('\n')

        ipaddress = re.findall(r'\d*.\d*.\d*.\d*', temp)[0]
        conf[26] = ipaddress + "\n"
        
            # Write to subterfuge.conf
        with open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'w') as file:
            file.writelines(conf)

      
        print "Starting Pwn Ops..."
        os.system("python " + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + "mitm.py -a &")
        
        # If Method not Auto
      else:
        print "Starting Pwn Ops..."
        os.system("python " + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + "mitm.py -a &")
    else:            
        print "Nope... Chuck Testa!"
        
def stoppwn(request):
    if request.is_ajax():
        print "Ceasing Pwn Ops..."
        cease()
    else:
        print "Nope... Chuck Testa!"
        
def resetpwn(request):
    if request.is_ajax():
        print "Resetting Pwn DB..."
            #For MySQL
        #cmd = "mysql --force harvester -u root -ppass < /harvester/templates/flush.sql"
        cmd = "cp " + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + "/base_db " + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + "/db"
        os.system(cmd)
    else:            
        print "Nope... Chuck Testa!"
        
def gate(request):
   if request.is_ajax():
      print "Loading Default Gateway"
      f = os.popen("ifconfig " + interface + " | grep \"inet addr\" | sed -e \'s/.*addr://;s/ .*//\'")
      temp = ''
      temp2 = ''
      temp3 = ''
      temp = f.readline().rstrip('\n')
      temp2 = re.findall(r'\d*.\d*.\d*.', temp)
      temp3 = temp2[0]
      temp3 = temp3 + '1'
		
	      #Relay Template Variables
      return render_to_response("includes/gateway.inc", {
      "gateway"    :   temp3,
      })
   else:            
      print "Nope... Chuck Testa!"
      
      

        
