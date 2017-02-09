from pywinauto.application import Application
import subprocess
#NOTE: Python 2.7.13 fails import of pywinauto (http://pywinauto.github.io/)
#library: Issue29294  ctypes.windll.LoadLibrary refuses unicode argument
#Therefore use 2.7.12 (or Python 3) or wait for 2.7.14 where it will be fixed ( http://bugs.python.org/issue29294)

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
print file.read()

#from pywinauto.application import Desktop
appAion = Application().start(r"C:\TEMP\examples\Associate\associate.bin\_associate.exe")
#appAion.print_control_identifiers()
print("Second round")
dlg = appAion['Title']
dlg.print_control_identifiers()
appAion[u'Title']['OK'].print_control_identifiers()
print ("------------ **** ------------")
appAion[u'Title']['OK'].close()
print ("------------ **** ------------")
appAion[u'Title']['OK'].click()
appAion[u'Title']['OK'].print_control_identifiers()
appAion[u'Title']['OK'].click()
appAion[u'Title']['OK'].print_control_identifiers()
appAion[u'Title']['OK'].click()
appAion[u'Title']['OK'].print_control_identifiers()
appAion[u'Title']['OK'].click()
appAion[u'Title']['OK'].print_control_identifiers()
appAion[u'Title']['OK'].click()
appAion[u'Title']['OK'].print_control_identifiers()
appAion[u'Title']['OK'].click()
appAion[u'Title']['OK'].print_control_identifiers()
appAion[u'Title']['OK'].click()
appAion[u'Title']['OK'].print_control_identifiers()
appAion[u'Title']['OK'].click()


print ("done with test")
