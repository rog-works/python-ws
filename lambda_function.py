# -*- coding: utf-8 -*-

from app.config import Config
from app.awslambda import AwsLambda as App

def lambda_function(event, context):
	return App(Config('config/app-dev.yml')).run(event)
