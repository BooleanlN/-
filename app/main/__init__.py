# -*- coding:utf-8 -*-
"""
@author liuning
@date 2019/6/16 14:14
@File __init__.py.py 
@Desciption
"""
from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes