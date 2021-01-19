import os
import subprocess


def sF(cmd):
    os.startfile(cmd)

def sFMaya(action):
    if action == "open":
        path = "C:/Program Files/Autodesk/Maya2020/bin/maya.exe"
        os.startfile(path)
    
    if action == "close":
        try:
            os.system("TASKKILL /F /IM maya.exe")
        except:
            pass