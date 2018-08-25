# -*- coding: utf-8 -*-

from application import Application

def lambda_function(event, context):
	return Application(event).run()
