# -*- coding:utf-8 -*-
"""
@author liuning
@date 2019/6/16 15:21
@File routes.py 
@Desciption
"""

from app import db
from flask import request, json, session
from app.models import User
from app.auth import bp
import uuid

@bp.route('/login',methods=['POST'])
def login():
    """
    login 接口
    :return: payload
    """
    username = request.form.get('username')
    password = request.form.get('password')
    res = {}
    user = User.query.filter_by(username=username).first()
    if user and request.method == 'POST':
        if user.check_password(password):
            res['code'] = 1
            res['msg'] = "login success"
            sessionId = str(uuid.uuid1())
            session[sessionId] = username
            res['data'] = {"session": sessionId}
        else:
            res['code'] = -1
            res['msg'] = "Invalid username or password"
    else:
        res['code'] = -1
        res['msg'] = "Invalid username or password"
    return json.dumps(res, encoding="utf-8")

@bp.route('/logout',methods=['POST'])
def logout():
    """
    登出 接口
    :return: 
    """
    sessionId = request.form.get('session')
    if sessionId:
        #session.pop(sessionId)
        payload = {'code':1,'msg':'logout success'}
        return json.dumps(payload,encoding="utf-8")
    payload = {'code':-1,'msg':'logout failed'}
    return json.dumps(payload,encoding="utf-8")

@bp.route('/registe',methods=['GET','POST'])
def registe():
    """
    注册接口
    :return: 
    """
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    payload = {}
    if user is None:
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        payload['code'] = 1
        payload['msg'] = "registe success"
    else:
        payload['code'] = -1
        payload['msg'] = "please choose another username"
    return json.dumps(payload, encoding="utf-8")