# -*- coding: utf-8 -*-

from app.awslambda import AwsLambda as App

def lambda_function(event, context):
	return App().run(event)
