# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

from data.config import Config
from app.awslambda import AwsLambda as App

def lambda_handler(event, context):
	return App().run(Config('config/app-dev.yml'), event)
