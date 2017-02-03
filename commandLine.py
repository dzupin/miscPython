#import subprocess32 as subprocess
#import os

import subprocess
#subprocess.call("ls -al >> mylogfile.log", shell=True)
#subprocess.call("date >> mylogfile.log", shell=True)
#subprocess.call("pwd >> mylogfile.log", shell=True)




subprocess.call("cd;pwd", shell=True)
#subprocess.call(["pwd;cd /TEMP;pwd"], shell=True)
subprocess.call("pwd")
subprocess.call(["ls", "-l"])  # doesn't capture output


#proc = subprocess.Popen(['tail', '-500', '/TEMP/mylogfile.log'], stdout=subprocess.PIPE)
proc = subprocess.Popen(['tail', '-2','/TEMP/mylogfile.log'], stdout=subprocess.PIPE)
for line in proc.stdout.readlines():
    print (line.rstrip())


#if os.name == 'posix' and sys.version_info[0] < 3:
#    import subprocess32 as subprocess
#else:
#    import subprocess
#print subprocess.check_output(['ls','-l'])
#print subprocess.check_output(['pwd'])

#cmd = 'whoami;date;pwd;'
#os.system(cmd)

#cmd2 = 'whoami;date;pwd'
#os.system(cmd2)

#os.system('whoami;date;pwd;date;date;date')