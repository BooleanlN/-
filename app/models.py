# -*- coding:utf-8 -*-
"""
@author liuning
@date 2019/6/16 14:07
@File models.py.py 
@Desciption
"""
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from app import db

class User(db.Model):
    """
    用户
    """
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),index=True,unique=True)
    password_hash = db.Column(db.String(128))
    #外键，可联合查询
    def __repr__(self):#返回一个可以用来表示对象的可打印字符串
        return '<User {}>'.format(self.username)
    def set_password(self,password):
        self.password_hash = generate_password_hash(password=password)
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    def get_id(self):
        return self.id
class Fault(db.Model):
    fault_id = db.Column(db.Integer, primary_key=True)
    fault_phoenoma = db.Column(db.String(1024))
    fault_reason = db.Column(db.Text(1024))
    fault_handle = db.Column(db.Text(1024))
    check_time = db.Column(db.DateTime,index=True,default=datetime.now())

    def __repr__(self):  # 返回一个可以用来表示对象的可打印字符串
        return '<Fault {}>'.format(self.fault_id,self.fault_phoenoma,self.fault_reason,self.fault_handle)

class LowPowerUser(db.Model):
    low_power_user_id = db.Column(db.Integer, primary_key=True)
    low_power_user_name = db.Column(db.String(64))
    ele_cosumption = db.Column(db.Float)
    ele_consumption_abnormal_level = db.Column(db.Integer,default=0)
    check_time = db.Column(db.DateTime,index=True,default=datetime.now(),primary_key=True)
    def __repr__(self):  # 返回一个可以用来表示对象的可打印字符串
        return '<LowPowerUser {}>'.format(self.low_power_user_id,self.low_power_user_name,self.ele_cosumption,self.ele_consumption_abnormal_level)
