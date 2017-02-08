#NOTE: Python 2.7.13 fails import of pywinauto library: Issue29294  ctypes.windll.LoadLibrary refuses unicode argument
#      Therefore use 2.7.12 (or Python 3) or wait for 2.7.14 where it will be fixed ( http://bugs.python.org/issue29294)
from pywinauto.application import Application

app = Application().start("C:\\Windows\\Notepad.exe")

app.UntitledNotepad.menu_select("Help->About Notepad")
app.AboutNotepad.OK.click()
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
