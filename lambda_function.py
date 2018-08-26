# -*- coding: utf-8 -*-

from data.config import Config
from app.awslambda import AwsLambda as App

def lambda_function(event, context):
	return App().run(Config('config/app-dev.yml'), event)
