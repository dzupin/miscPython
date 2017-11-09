import sys     # Used to retrieve Python version number (to select between Python2 or Python3 specific code)

if sys.version_info[0] < 3:
    import _winreg as wreg  #For Python 2.x
else:
    import winreg as wreg  # For Python 3.X

# Create new registry key with subkey and new value - Reenable next 3 lines when this code is run for the first time
#key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "Software\\TestCompany\\TestProject")
#wreg.SetValue(key, 'NewSubkey', wreg.REG_SZ, 'testsubkey')
#wreg.SetValueEx(key, 'ValueName', 0, wreg.REG_SZ, 'testvalue')

key = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, "Software\\TestCompany\\TestProject",0, wreg.KEY_ALL_ACCESS)
print ("Next line should output: testsubkey")
print (wreg.QueryValue(key, 'NewSubkey'))
print ("Next line should output: testvalue")
print (wreg.QueryValueEx(key, 'ValueName'))
key.Close()
