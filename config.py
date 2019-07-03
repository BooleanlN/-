# -*- coding:utf-8 -*-
"""
@author liuning
@date 2019/6/16 14:05
@File config.py.py 
@Desciption
"""
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = '123456'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'oracle://System:1234@localhost:1521/ORCL'
    HOST='0.0.0.0'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ['wuhan']
    # SESSION_TYPE = os.environ.get('SESSION_TYPE') or 'nowhere'
    # SESSION_REDIS = redis.Redis(host=os.environ.get('SESSION_REDIS_SEVER'),port=os.environ.get('SESSION_REDIS_PORT'))
    SESSION_KEY_PREFIX = os.environ.get('SESSION_KEY_PREFIX') or 'flask'