from __future__ import print_function
from pywinauto.application import Application
import subprocess
import sys
import time
import os
from threading import Timer

#Set-up default values
testAppDirectory = "C:\TEMP\examples"
testAppName = "Associate"


'''Function definition and invocation for respawn.exe availability on the end user system.'''
def checkAvailabilityOfRespawn():
    #INVOKE PROGRAM
    try:
        #Generate respawn dialog box and if successfull then report success in "exception" block
        #When AionBRE is correcly installed, respawn.exe is accessible from system path.
        #Set of Timeout is mandatory otherwise script will not process rest of the code. NOTE: Timeout not in Python 2.7
        respawnCheckpoint = subprocess.call("respawn.exe", shell=True, timeout=2)
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

'''Function definition and invocation for reexec.exe availability on the end user system.'''
def checkAvailabilityOfReexec():
    # INVOKE PROGRAM
    try:
         # Generate respawn dialog box and if successfull then report success in "exception" block
            # When AionBRE is correcly installed, respawn.exe is accessible from system path.
            # Set of Timeout is mandatory otherwise script will not process rest of the code. NOTE: Timeout not in Python 2.7
            respawnCheckpoint = subprocess.call("reexec.exe", shell=True, timeout=1)
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



def BuildAionApp(testAppName):
    if not(os.path.isdir(testAppDirectory + "\\" + testAppName)):
        print ("Failed to find test application directory")
        print ("Exit code 3: The system cannot find the path specified.")
        return (3)
    if not(os.path.exists(testAppDirectory + "\\" + testAppName + "\\" + testAppName + ".app" )):
        print ("Failed to find test application directory")
        print ("Exit code 2: The system cannot find the file specified.")
        return (2)
    goToTestExample = "cd  " + testAppDirectory + "\\" + testAppName + " && "
    deleteOldLogsAndTestFiles = "rmdir " + testAppName + ".bin /s /q  &  del " + testAppName + ".log & dir > " + testAppName + ".log && "
    respawnApp = "respawn associate.app >> " + testAppName + ".log  2>&1"
    print("In the next step I will run respawn in command line")
    cmdTestRoutineWin = goToTestExample + deleteOldLogsAndTestFiles + respawnApp
    print(cmdTestRoutineWin)

    try:
        subprocess.call(cmdTestRoutineWin, shell=True, timeout=3)
    except Exception:
        print("Fail to start your test application")
        print("Because of Error when attempting to start test application this test run will be aborted ... ")
        #   sys.exit(8)

    # Check for specific Dialog box window that in this case indicate missing test file
    try:
        appCheckPoint = Application().Connect(title='Aion Build Utility')
    except Exception:
        print("Everything seems to be fine with respawn")

    try:
        appCheckPoint
        if appCheckPoint.window(title='Aion Build Utility').Exists():
            print("Aion Build Utility Error")
            # If detected dialog exists it should be closed othewise it polute client desktop afte test exits
            appCheckPoint['Dialog']['Button'].click()
    except NameError:
        print("Everything is fine with running respawn command")
    except Exception:
        print("Something else went wrong")
    print("file open checkpoint")
    print(testAppDirectory + "\\" + testAppName + ".log")
    file = open(testAppDirectory + "\\" + testAppName + "\\" + testAppName + ".log", 'r')
    print(file.read())

    print("Finished building test application")
    print (testAppName)




def ReexecAionApp(testAppName):
    try:
        if not (os.path.exists(testAppDirectory + "\\" + testAppName + "\\" + testAppName + ".app")):
            print("Failed to find test application script app file")
            print("Exit code 2: The system cannot find the file specified.")
            exit(2)
        # We verified that app file exist and now lets try to process/interpret it with reecec
        appAion = Application().start(r"reexec " + testAppDirectory + "\\" + testAppName + "\\" + testAppName + ".app")
        while not appAion.Windows_():
            time.sleep(.5)
    except Exception:
        # Because appAion generated window will be present even if reexec reports failure, this will only fail if reexec itself fails to run
        print("Generic exception: Application failed to start")
        print("Error code 22: The device does not recognize the command.")
        exit(22)
    except:
        print("something else went wrong")
        sys.exit()
    print("Started test application run ...")
    while appAion['Dialog'].Exists():
        # Optional time delay
        time.sleep(.5)
        print(appAion['Dialog']['Static'].Texts())
        appAion['Dialog']['Button'].click()
    print("Done with reexec test")


def RunCompiledAionApp(testAppName):
    try:
        if not (os.path.exists(testAppDirectory + "\\" + testAppName + "\\" +  testAppName + ".bin" + "\\" + "_" + testAppName + ".exe")):
            print("Failed to find test application binary")
            print("Exit code 2: The system cannot find the file specified.")
            print (testAppDirectory + "\\" + testAppName + "\\" +  testAppName + ".bin" + "\\" + "_" + testAppName + ".exe")
            exit(2)
        # We verified that app file exist and now lets try to process/interpret it with reecec
        appAion = Application().start(testAppDirectory + "\\" + testAppName + "\\" + testAppName + ".bin"+ "\\" + "_" + testAppName + ".exe")
        while not appAion.Windows_():
            time.sleep(.5)
    except Exception:
        # Because appAion is already tested for availability, this will only fail if binary itself fails to run
        print("Generic exception: Application binary failed to start")
        print("Error code 22: The device does not recognize the command.")
        exit(22)
    except:
        print("something else went wrong")
        sys.exit()
    print("Started test application run ...")
    while appAion['Dialog'].Exists():
        # Optional time delay
        time.sleep(.5)
        print(appAion['Dialog']['Static'].Texts())
        appAion['Dialog']['Button'].click()
    print("Done with binary run test")






#################################################   TESTING ############################################################
#Prereq
#AionBRE installed, Aion examples directory located in C:\TEMP
#Step 1. Check correct functionality of  respawn.exe
#Step 2. Check correct functionalituy of reexec.exe
#Step 3. Build Aion Test Application
#Step 4. Run Aion Test Application in Interpretive mode (reexec)
#Step 5. Run Test Application compiled binary file

#Step 1
checkAvailabilityOfRespawn()

#Step 2
checkAvailabilityOfReexec()

#Step 3
BuildAionApp("Associate")
#check if invalid app name is correctly handled
BuildAionApp("Associate333")
BuildAionApp("Associate")

#Step 4
ReexecAionApp("Associate")

#Step 5
RunCompiledAionApp("Associate")

print ("Test Completed.")

########################################################################################################################
