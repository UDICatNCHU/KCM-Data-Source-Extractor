#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KCM generating script

This script is used to generate KCM/TCM (Term correlated model).
The task is done by calling many other scripts
"""
import os, subprocess, sys, logging
from pathlib import Path
class KCM(object):
    """docstring for KCM"""
    def __init__(self):
        pass
        
    def download(self, lang, io_dir):
        import subprocess
        io_dir = os.path.join(io_dir, lang)

        subprocess.call(['bash', os.path.join('langConfig', lang+'.sh'), os.getcwd()])
        print(os.getcwd())

def hasFile():
        file = Path('wiki.txt.all')
        if file.is_file():
            return True
        else: return False


if __name__ == '__main__':
    if hasFile():
        os.remove('wiki.txt.all')
    with open('wiki.txt.all', "a") as outfile:
        for (dir_path, dir_names, file_names) in os.walk('WikiRaw/cht'):
            print(dir_path, dir_names, file_names)
            if file_names != []:
                for f in file_names:
                    subprocess.call(['cat', os.path.join(dir_path, f)], stdout=outfile)
