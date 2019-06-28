# -*- coding:utf-8 -*-
"""
@author liuning
@date 2019/6/16 15:18
@File __init__.py.py 
@Desciption
"""
from flask import Blueprint

bp = Blueprint('manage',__name__)

from app.manage import routes