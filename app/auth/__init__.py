# -*- coding:utf-8 -*-
"""
@author liuning
@date 2019/6/16 15:21
@File __init__.py.py 
@Desciption
"""
from flask import Blueprint

bp = Blueprint('auth',__name__)

from app.auth import routes