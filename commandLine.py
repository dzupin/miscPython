import subprocess
####import subprocess32 as subprocess

# Setup your execution command
goToInstallDir="cd /opt/CA/AionBRE;"
initializeEnvironment=". ./aion.sh;"
goToTestExample="cd /opt/CA/AionBRE/examples/Associate;"
deleteOldLogsAndTestFiles= "rm /TEMP/Out.log; rm -rf /opt/CA/AionBRE/examples/Associate/associate.bin;"
respawnApp= "  respawn associate.app >> /TEMP/Out.log  2>&1;"
reexecRun= "reexec associate >> /TEMP/Out.log 2>&1 ;"
binaryRun= "cd associate.bin;./_associate >> /TEMP/Out.log 2>&1 "

#Put together execution command
cmdTestRoutine=goToInstallDir + initializeEnvironment + goToTestExample + deleteOldLogsAndTestFiles + respawnApp + reexecRun + binaryRun

#Run econcatenated execution commnand
subprocess.call(cmdTestRoutine,shell=True)

#Example how to open and parse log file using shell command tail on Linux (If possible, use Python build-in file processing instead)
proc = subprocess.Popen(['tail', '-2000','/TEMP/Out.log'], stdout=subprocess.PIPE)
for line in proc.stdout.readlines():
    print (line.rstrip())



#Scratchpad AREA
#  import os
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