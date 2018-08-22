# -*- coding: utf-8 -*-

import yaml
import re

# load mapping data
f = open('mapping.yaml', 'r')
data = yaml.load(f)
f.close()

# create context
context = {"id": 1, "code": 2, "message": {"1":1,"2":2,"3":3}}

# evaluate convert script
result = {}
for key, value in data['/path/to.workspace']['to'].items():
	script = value
	if re.match(r"^[\w\[\]\']+$", script):
		script = '_ret = {}'.format(script)
	elif re.search(r'(\s*)return\s+(.+)', script, flags=re.MULTILINE):
		script = re.sub(r'(\s*)return\s+(.+)', r'\1_ret = \2', script, flags=re.MULTILINE)
	else:
		script = "_ret = '{}'".format(script)
	exec(script, {}, context)
	result[key] = context['_ret']

# show result
print(result)
