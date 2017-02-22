#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from crawler import *
import json, sys
# example : crawler(['-b', 'PublicServan', '-i', '100', '101'])
argvs = sys.argv[1:]
filename = crawler(argvs)
with open('ptt.kcm', 'w', encoding='utf-8') as f:
	for i in map(lambda x:x.get('content', ''), json.load(open(filename, 'r'))['articles']):
		f.write(i + '\n')