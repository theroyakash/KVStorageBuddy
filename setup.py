import sys
from cx_Freeze import setup, Executable

base = None
base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable("gui_service.py", base=base, target_name="KeyValueStoreApp")
]

setup(
    name="KVStorageBuddy",
    version="1.69.420",
    description="KeyValueStoreApp is a common text storage application",
    executables=[Executable("gui_service.py")]
)
