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
	source = value
	if re.match(r"^[\w\[\]\']+$", source):
		source = '_ret = {}'.format(source)
	elif re.search(r'(\s*)return\s+(.+)', source, flags=re.MULTILINE):
		source = re.sub(r'(\s*)return\s+(.+)', r'\1_ret = \2', source, flags=re.MULTILINE)
	exec(source, {}, context)
	result[key] = context['_ret']

# show result
print(result)
