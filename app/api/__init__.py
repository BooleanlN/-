# -*- coding:utf-8 -*-
"""
@author liuning
@date 2019/6/16 14:04
@File __init__.py.py 
@Desciption
"""
import os

from flask import Blueprint

LOCAL_DIRECTORY_PATH = os.getcwd() + "/" #当前文件路径
bp = Blueprint('api',__name__)

from . import excelroutes