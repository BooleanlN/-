# -*- coding:utf-8 -*-
"""
@author liuning
@date 2019/6/16 15:19
@File routes.py 
@Desciption
"""
from flask import request, json
from sqlalchemy import desc

from app.manage import bp
from app import db
from app.models import User,LowPowerUser

@bp.route('/userList', methods=['POST'])
def getUserList():
    """
    :return: json，用户列表查询接口
    """
    page_no = request.form.get('pageno')
    page_size = request.form.get('pagesize')
    user_list_page = User.query.paginate(int(page_no),int(page_size))
    user_list = user_list_page.items
    page_count = user_list_page.pages
    res = []
    payload = {}
    for user in user_list:
        user_item = {"username": user.username}
        res.append(user_item)
    payload["code"] = 1
    payload["data"] = res
    payload["msg"] = "success"
    payload["pagecount"] = page_count
    payload["pageno"] = page_no
    return json.dumps(payload, encoding="utf-8")


@bp.route('/userDelete', methods=['POST'])
def deleteUser():
    """
    删除用户
    :return: json,删除用户接口
    """
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    payload = {}
    if user is None:
        payload['code'] = -1
        payload['msg'] = 'delete fail'
        payload['data'] = []
    else:
        db.session.delete(user)
        db.session.commit()
        payload['code'] = 1
        payload['msg'] = 'delete success'
        payload['data'] = []
    return json.dumps(payload, encoding="utf-8")


@bp.route('/userConfig', methods=['POST'])
def setSaveConfig():
    """
    用户设置接口
    :return: 
    """
    saveposition = request.form.get("position")
    imgposition = request.form.get("imgposition")
    textposition = request.form.get("textposition")
    payload = {}
    payload['code'] = 1
    payload['msg'] = '设置保存成功'
    payload['data'] = []
    return json.dumps(payload, encoding="utf-8")

@bp.route('/lowpowerusertable',methods=['POST'])
def get_low_power_user_list():
    """
    得到低电量用户列表
    :return: 
    """
    page_no = request.form.get('pageno')
    page_size = request.form.get('pagesize')
    #分页查询
    lowpoweruserpage = LowPowerUser.query.paginate(int(page_no),int(page_size))
    lowpoweruserlist = lowpoweruserpage.items
    page_count = lowpoweruserpage.pages

    payload = {}
    userlist = []
    if len(lowpoweruserlist) is not 0:
        low_user_count = LowPowerUser.query.filter(LowPowerUser.low_power_user_name is not None).count()
        low_user_max_consumption = LowPowerUser.query.order_by(desc(LowPowerUser.ele_cosumption)).first().ele_cosumption
        low_user_max_grade = LowPowerUser.query.order_by(desc(LowPowerUser.ele_consumption_abnormal_level)).first().ele_consumption_abnormal_level
    else:
        low_user_count = 0
        low_user_max_consumption = 0
        low_user_max_grade = 0
    for lowpoweruser in lowpoweruserlist:
        print(lowpoweruser)
        lowpoweruserobj = {}
        lowpoweruserobj['lowpowerusername'] = lowpoweruser.low_power_user_name
        lowpoweruserobj['lowpowerusereleconsumption'] = lowpoweruser.ele_cosumption
        lowpoweruserobj['lowpoweruserlevel'] = lowpoweruser.ele_consumption_abnormal_level
        userlist.append(lowpoweruserobj)
    payload['data'] = userlist
    payload['pagecount'] = page_count
    payload['pageno'] = int(page_no)
    payload['usercount'] = low_user_count
    payload['maxdayilyconsumption'] = low_user_max_consumption
    payload['maxdayilygrade'] = low_user_max_grade
    payload['code'] = 1
    payload['msg'] = '查询成功'
    return json.dumps(payload,encoding="utf-8")

@bp.route('/lowpowerusers',methods=['POST'])
def insert_low_power_user():
    """
    插入低电量用户
    :return: 
    """
    payload = {}
    username = request.form.get('lowpowerusername')
    usereleconsumption = request.form.get('eleconsumption')
    usereleconsumptionlevel = request.form.get('eleconsumptionlevel')

    lowpoweruser = LowPowerUser(low_power_user_name=username,ele_cosumption=usereleconsumption,ele_consumption_abnormal_level=usereleconsumptionlevel)
    db.session.add(lowpoweruser)
    r = db.session.commit()
    print(r)
    payload['code']  = 1
    payload['msg'] = '插入成功'
    payload['data'] = []
    return json.dumps(payload,encoding="utf-8")

@bp.route('/lowpowerusersdelete', methods=['POST'])
def delete_low_power_user():
    """
    删除某低压用户
    :return: 
    """
    username = request.form.get('username')
    user = LowPowerUser.query.filter_by(low_power_user_name=username).first()
    print(LowPowerUser.low_power_user_name)
    payload = {}
    if user is None:
        payload['code'] = -1
        payload['msg'] = 'delete fail'
        payload['data'] = []
    else:
        db.session.delete(user)
        db.session.commit()
        payload['code'] = 1
        payload['msg'] = 'delete success'
        payload['data'] = []
    return json.dumps(payload, encoding="utf-8")
