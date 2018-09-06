import cx_Freeze
import sys
import os

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"

base = None
if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("tk-standup.py", base=base, icon=r"C:\Users\kai_p\OneDrive\Documents\GitHub\solo-standup\favicon.ico")]

cx_Freeze.setup(
    name = "Standups",
    options = {"build.exe": {"packages": ["tkinter", "PIL"], "include_files": ["favicon.ico", "logo.png"]}},
    version = "0.1",
    description = "Simple Standup app",
    executables = executables
    )