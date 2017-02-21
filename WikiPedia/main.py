#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KCM generating script

This script is used to generate KCM/TCM (Term correlated model).
The task is done by calling many other scripts
"""
import os, logging
class KCM(object):
    """docstring for KCM"""
    def __init__(self):
        pass
        
    def download(self, lang, io_dir):
        import subprocess
        io_dir = os.path.join(io_dir, lang)

        subprocess.call(['bash', os.path.join('langConfig', lang+'.sh'), os.getcwd()])
        print(os.getcwd())

if __name__ == '__main__':
    k = KCM()
    k.download('cht', 'WikiRaw/')