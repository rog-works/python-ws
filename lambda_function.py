# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

from data.config import Config
from app.lambdaapp import LambdaApp as App

def lambda_handler(event, context):
	config = Config(f'config/app-{os.environ["ENV"]}.yml')
	return App().run(config, event)
