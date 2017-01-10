# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from _winreg import *
import re
import os


def getSVNPath():
    svnPath = ""
    try:
        updates = r'svn\shell\open'
        aReg = ConnectRegistry(None,HKEY_CLASSES_ROOT)
        key = OpenKey(HKEY_CLASSES_ROOT, updates)
        value = QueryValue(key,"command")
        pattern = re.compile(r"^.*exe(?=.*)")
        match = pattern.match(value)
        if match:
            # 使用Match获得分组信息
            svnPath = match.group()
            return svnPath
    except:
        return svnPath

print getSVNPath()

if __name__ == "__main__":
    svnPath = getSVNPath()
    isFrist = True
    cmd = '"'+svnPath + '"'
    for arg in sys.argv:
        if isFrist:
            isFrist = False
            continue
        cmd = cmd + " " + arg

    print cmd
    os.system(cmd)
