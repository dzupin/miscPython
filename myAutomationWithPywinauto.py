from __future__ import print_function
from pywinauto.application import Application
import subprocess
import sys
import time
#NOTE: Python 2.7.13 fails import of pywinauto (http://pywinauto.github.io/)
#library: Issue29294  ctypes.windll.LoadLibrary refuses unicode argument
#Therefore use 2.7.12 (or Python 3) or wait for 2.7.14 (fix is in nightbuild) ( http://bugs.python.org/issue29294)

#Commented out Notepad sample demon. Uncomment it, in case you need to check functionality of the pywinauto library ####
#app = Application().start("C:\\Windows\\Notepad.exe",timeout=1)
#app.UntitledNotepad.menu_select("Help->About Notepad")
#app.AboutNotepad.OK.click()
##app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
#app.UntitledNotepad.type_keys("%FX")
########################################################################################################################


#Aion testing
goToTestExample="cd  C:\TEMP\examples\Associate &&"
deleteOldLogsAndTestFiles= "rmdir associate.bin /s /q  &  del Out.log & dir > Out.log &&"
respawnApp= "  respawn associate.app >> Out.log  2>&1 "
cmdTestRoutineWin= goToTestExample + deleteOldLogsAndTestFiles + respawnApp
subprocess.call(cmdTestRoutineWin,shell=True)

file = open('C:\TEMP\examples\Associate\Out.log', 'r')
print (file.read())

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
    print("Because test app is not available we should exit the test")
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
