# -*- coding:utf-8 -*-
"""
@author liuning
@date 2019/6/16 14:14
@File routes.py 
@Desciption
"""
from flask import render_template

from app.main import bp
"""
主页接口
"""
#主页
@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')

@bp.route('/manage')
def manage():
    return  render_template('index.html')