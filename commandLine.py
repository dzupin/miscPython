import subprocess32 as subprocess
#if os.name == 'posix' and sys.version_info[0] < 3:
#    import subprocess32 as subprocess
#else:
#    import subprocess
print subprocess.check_output(['dir','/Q'])