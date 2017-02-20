from __future__ import print_function
from pywinauto.application import Application
import subprocess
import sys
import time
from threading import Timer



'''Function definition and invocation for respawn.exe availability on the end user system.'''
def checkAvailabilityOfRespawn():
    #INVOKE PROGRAM
    try:
        #Generate respawn dialog box and if successfull then report success in "exception" block
        #When AionBRE is correcly installed, respawn.exe is accessible from system path.
        #Set of Timeout is mandatory otherwise script will not process rest of the code. NOTE: Timeout not in Python 2.7
        respawnCheckpoint = subprocess.call("respawn.exe", shell=True, timeout=1)
    except Exception:
        print("Found respawn.exe ... ")
    #CLEAN-UP
    #Respawn execution will automatically create dialog box. We need to close this no longer needed dialog box.
    try:
        #Check if connection to respawn.exe generated dialog box is possible
        appCheckPoint = Application().Connect(title='Build Aion Application')
        #Verified that respawn.exe generated dialog box exists and now that test is done I need to remove it (clean up).
        if appCheckPoint.window(title='Build Aion Application').Exists():
            appCheckPoint['Dialog']['Cancel'].click()
        print("Aion Build Utility is available and functional")
    #ERROR PROCESSING
    except Exception:
        #Something went wrong. Report problem (most likely repawn is not installed or not in system path)
        print("respawn.exe (Aion Build Utility) is not available on targeted system.")
        print("Return code 197: The operating system is not presently configured to run respawn application.")
        exit(197)

    '''Function definition and invocation for respawn.exe availability on the end user system.'''

def checkAvailabilityOfReexec():
    # INVOKE PROGRAM
    try:
         # Generate respawn dialog box and if successfull then report success in "exception" block
            # When AionBRE is correcly installed, respawn.exe is accessible from system path.
            # Set of Timeout is mandatory otherwise script will not process rest of the code. NOTE: Timeout not in Python 2.7
            respawnCheckpoint = subprocess.call("reexec999.exe", shell=True, timeout=1)
    except Exception:
        print("Found reexec.exe ... ")
        # CLEAN-UP
        # Reexec execution will automatically create dialog box. We need to close this no longer needed dialog box.
    try:
        # Check if connection to respawn.exe generated dialog box is possible
        appCheckPoint = Application().Connect(title='Run Aion Application')
        # Verified that reexec.exe generated dialog box exists and now that test is done I need to remove it (clean up).
        if appCheckPoint.window(title='Run Aion Application').Exists():
            appCheckPoint['Dialog']['Cancel'].click()
        print("Run Aion Application is available and functional")
    # ERROR PROCESSING
    except Exception:
        # Something went wrong. Report problem (most likely repawn is not installed or not in system path)
        print("reexec.exe (Run Aion Application) is not available on targeted system.")
        print("Return code 197: The operating system is not presently configured to run reexec application.")
        exit(197)




#Prereq
#AionBRE installed, Aion examples directory located in C:\TEMP
#Step 1. Check correct functionality of  respawn.exe
#Step 2. Check correct functionalituy of reexec.exe

#Call respawn.exe functionality check
checkAvailabilityOfRespawn()
checkAvailabilityOfReexec()






exit (0)
#Aion testing
goToTestExample="cd  C:\TEMP\examples\Associate &&"
deleteOldLogsAndTestFiles= "rmdir associate.bin /s /q  &  del Out.log & dir > Out.log &&"
respawnApp= "respawn associate999.app >> Out.log  2>&1"
print ("In the next step I will run respawn in command line")
cmdTestRoutineWin= goToTestExample + deleteOldLogsAndTestFiles + respawnApp
print (cmdTestRoutineWin)

try:
    subprocess.call(cmdTestRoutineWin, shell=True,timeout=3)
except Exception:
    print("Fail to start your test application")
    print ("Because of Error when attempting to start test application this test run will be aborted ... ")
 #   sys.exit(8)

#Check for specific Dialog box window that in this case indicate missing test file
try:
    appCheckPoint = Application().Connect(title='Aion Build Utility')
except Exception:
    print ("Everything seems to be fine with respawn")

try:
    appCheckPoint
    if appCheckPoint.window(title='Aion Build Utility').Exists():
        print("Aion Build Utility Error")
        #If detected dialog exists it should be closed othewise it polute client desktop afte test exits
        appCheckPoint['Dialog']['Button'].click()
except NameError:
    print ("Everything is fine with running respawn command")
except Exception:
    print ("Something else went wrong")

file = open('C:\TEMP\examples\Associate\Out.log', 'r')
print (file.read())


print ("Show must go on")
exit (88)

#from pywinauto.application import Desktop
try:
    #appAion = Application().start(r"C:\TEMP\examples\Associate\associate.bin\_associate.exe")
    appAion = Application().start(r"reexec C:\TEMP\examples\Associate\associate.app")
    #Delay timer for applications that may be slower to initialize their GUI
    while not appAion.Windows_():
        time.sleep(.5)
except Exception:
    print ("Generic exception: Application failed to start")
except:
    print ("something else went wrong")
    sys.exit()
#appAion.print_control_identifiers()
print("Second round")


#Check for specific Dialog box window that in this case indicate missing test file
if appAion.window(title = "Aion Init").Exists():
    print ("Aion script that you are referencing does not exist.")
    print(appAion['Dialog'].Texts())
    print(appAion['Dialog']['Static'].GetProperties())
    print(appAion['Dialog']['Static'].Texts())
    print(appAion['Dialog']['Button'].Texts())
    print(appAion['Dialog'].capture_as_image().save("screen_capture_InitError.png", "PNG"))
    appAion['Dialog']['Button'].click()
    print("Because Aion respawn is not available we should exit the test")
    sys.exit()




dlg = appAion['Dialog']
dlg.print_control_identifiers()
appAion['Dialog']['Button'].print_control_identifiers()
print ("-------------------- **** -----------------------")
print (appAion['Dialog'].user_data())
#print appAion[u'Title'].Texts()                #[u'Title']
#print appAion[u'Title'].WindowText()           #Title
print (appAion['Dialog'].GetProperties())        #{u'is_enabled': True, u'is_visible': True, u'style': -1798831675, u'fonts': [<LOGFONTW 'Tahoma' -14>], u'client_rects': [<RECT L0, T0, R180, B132>], u'texts': [u'Title'], u'class_name': u'#32770', u'is_unicode': True, u'control_id': 0, u'user_data': 3847704, u'friendly_class_name': u'Dialog', u'control_count': 2, u'exstyle': 65793, u'context_help_id': 0, u'menu_items': [], u'rectangle': <RECT L908, T487, R1094, B649>}
#print appAion[u'Title'].user_data()            #3257504
#print appAion[u'Title'].Children()             #[<pywinauto.controls.win32_controls.ButtonWrapper object at 0x0000000006E6FA90>, <pywinauto.controls.win32_controls.StaticWrapper object at 0x0000000006E6FAC8>]
#print appAion[u'Title'].debug_message("My debug 1")  # writes debug message over control (see in saved PIL image) <pywinauto.controls.win32_controls.DialogWrapper object at 0x0000000006E6D0F0>
#print appAion[u'Title'].capture_as_image().save("screen_capture.png", "PNG")     #<PIL.Image.Image image mode=RGB size=186x162 at 0x6E72160>
print ("*****")
print (appAion['Dialog']['Static'].Texts())                #[[u'Error: Dissolve failed']
print ("++++")
#print appAion[u'Title']['OK'].Texts()             #[u'OK']
#print appAion[u'Title']['OK'].WindowText()        #OK
#print appAion[u'Title']['OK'].GetProperties()     #{u'is_enabled': True, u'is_visible': True, u'style': 1342373889, u'fonts': [<LOGFONTW 'Tahoma' -14>], u'client_rects': [<RECT L0, T0, R100, B30>], u'texts': [u'OK'], u'class_name': u'Button', u'is_unicode': True, u'control_id': 2, u'user_data': 0, u'friendly_class_name': u'Button', u'control_count': 0, u'exstyle': 4, u'context_help_id': 0, u'menu_items': [], u'image': <PIL.Image.Image image mode=RGB size=100x30 at 0x6F7C208>, u'rectangle': <RECT L983, T603, R1083, B633>}
#print appAion[u'Title']['OK'].user_data()         #0
#print appAion[u'Title']['OK'].Children()          #[]
#print appAion[u'Title']['OK'].debug_message("My debug 2")   # writes debug message over control (see in saved PIL image) <pywinauto.controls.win32_controls.ButtonWrapper object at 0x0000000006F0AC88>
#print appAion[u'Title']['OK'].capture_as_image().save("screen_capture2.jpg", "JPEG")  #<PIL.Image.Image image mode=RGB size=100x30 at 0x6E722E8>
print ("-------------------- **** -----------------------")
if appAion['Dialog'].Exists():
    print (appAion['Dialog']['Static'].Texts())
appAion['Dialog']['Button'].click()
if appAion['Dialog'].Exists():
    print (appAion['Dialog']['Static'].Texts())
appAion[u'dialog']['OK'].click()
if appAion['Dialog'].Exists():
    print (appAion['Title']['Static'].Texts())
appAion[u'Title']['OK'].click()
if appAion['Dialog'].Exists():
    print (appAion['Dialog']['Static'].Texts())
if appAion['Dialog'].Exists():
    appAion['Dialog']['Button'].click()

if appAion['Dialog'].Exists():
    print(appAion['Dialog']['Static'].Texts())
else:
    sys.exit()

print ("Continue .... ")
appAion['Dialog']['Button'].click()

while appAion['Dialog'].Exists():
    print ("inside of while loop")
    print(appAion['Dialog']['Static'].Texts())
    appAion['Dialog']['Button'].click()
else:
    print ("All is done ...")
    sys.exit()



print ("done with test")
