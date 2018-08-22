# -*- coding: utf-8 -*-

import yaml
import json
import re
from jsonschema import validate

# load mapping data
f = open('mapping.yaml', 'r')
data = yaml.load(f)
f.close()

print(json.dumps(data['/path/to.workspace']['schema']))

# create context
context = {
  "id": 1,
  "code": 2,
  "message": {
    "hoge": {
      "type": 1,
      "v": 2,
      "val": 3,
      "valts": 4
    }
  }
}

schema = {
  "type": "object",
  "properties": {
    "id": {"type": "integer"},
    "code": {"type": "integer"},
    "message": {
      "type": "object",
      "properties": {
        "type": "object",
        "additionalProperties": {
          "type": "object",
          "properties": {
            "type": {"type": "integer"},
            "v": {"type": "integer"},
            "valts": {"type": "integer"},
            "val": {"type": "integer"}
          }
        }
      }
    }
  }
}

print(json.dumps(schema))

# validate json schema
#validate({"id":1}, data['/path/to.workspace']['schema'])
validate(context, schema)

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
