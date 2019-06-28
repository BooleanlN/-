# -*- coding:utf-8 -*-
"""
@author liuning
@date 2019/6/16 14:09
@File excelroutes.py 
@Desciption
"""
from .utils import excelImport
from . import bp
from flask import request,json
from app import db
from app.models import Fault,User

@bp.route('/excel',methods=['POST'])
def excel_import_api():
    """
    excel批量导入接口
    :return: 
    """
    excel_files = request.files.getlist('excel')
    table_data = []
    payload = {}
    for excel in excel_files:
        table_data = excelImport(excel)
    for field_data in table_data:
        print(field_data)
        fault = Fault(fault_phoenoma=field_data['故障现象'],fault_reason=field_data['故障原因'],fault_handle=field_data['故障处理'])
        db.session.add(fault)
    db.session.commit()
    payload['code'] = 1
    payload['msg'] = '数据批量插入成功'
    payload['data'] =[]
    return json.dumps(payload)

@bp.route('/knowledgetable',methods=['POST'])
def get_knowledge_table():
    """
    获取知识列表
    :return: 
    """
    page_no = request.form.get('pageno')
    page_size = request.form.get('pagesize')
    faults_page = Fault.query.paginate(int(page_no),int(page_size))
    faults = faults_page.items
    page_count = faults_page.pages
    payload = {}
    fault_list = []
    result = {}
    # 知识库记录非空条数
    fault_apperence_len = Fault.query.filter(Fault.fault_phoenoma is not None).count()
    fault_handle_len = Fault.query.filter(Fault.fault_handle is not None).count()
    fault_reason_len = Fault.query.filter(Fault.fault_reason is not None).count()
    print(fault_reason_len)
    for fault in faults:
        fault_obj = {}
        fault_obj['faultApperence'] = fault.fault_phoenoma
        fault_obj['faultReason'] = fault.fault_reason
        fault_obj['faultHandle'] = fault.fault_handle
        fault_obj['faultid'] = fault.fault_id
        fault_list.append(fault_obj)
    result['data'] = fault_list
    result['fault_reason_count'] = fault_reason_len
    result['fault_handle_count'] = fault_handle_len
    result['fault_apperence_count'] = fault_apperence_len
    result['pagecount'] = page_count
    result['pageno'] = int(page_no)
    payload['data'] = result
    payload['code'] = 1
    payload['msg'] = '查询成功'
    return json.dumps(payload, encoding="utf-8")

@bp.route('/knowledge',methods=['POST'])
def insert_knowledge():
    """
    手动插入数据
    :return: 
    """
    fault_apperences = request.form.get('faultApperence').split(',')
    fault_reasons = request.form.get('faultReason').split(',')
    fault_handles = request.form.get('faultHandle').split(',')
    payload = {}
    for (fault_apperence,fault_reason,fault_handle ) in zip(fault_apperences,fault_reasons,fault_handles):
        fault = Fault(fault_phoenoma=fault_apperence,fault_reason=fault_reason,fault_handle=fault_handle)
        db.session.add(fault)
    db.session.commit()
    payload['code'] = 1
    payload['msg'] = '插入成功'
    payload['data'] = []
    return json.dumps(payload,encoding="utf-8")

@bp.route('/knowledgedelete', methods=['POST'])
def delete_knowledge():
    fault_id = request.form.get('faultid')
    fault = Fault.query.filter_by(fault_id=fault_id).first()
    payload = {}
    if fault is None:
        payload['code'] = -1
        payload['msg'] = 'delete fail'
        payload['data'] = []
    else:
        db.session.delete(fault)
        db.session.commit()
        payload['code'] = 1
        payload['msg'] = 'delete success'
        payload['data'] = []
    return json.dumps(payload, encoding="utf-8")
