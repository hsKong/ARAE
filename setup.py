import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","numpy","torch"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "console"
	#base = "Win32GUI"


setup(  name = "my prog",
    version = "1.0",
    description = "My application!",
    options = {"build_exe": build_exe_options},
    executables = [Executable("train_main1211.py", base = base)])