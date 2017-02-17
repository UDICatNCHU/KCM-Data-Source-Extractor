#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
with open('ptt.kcm', 'w', encoding='utf-8') as f:
	for i in map(lambda x:x['content'], json.load(open('ptt.json', 'r'))['articles']):
		f.write(i + '\n')