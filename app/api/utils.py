# -*- coding:utf-8 -*-
"""
@author liuning
@date 2019/6/16 14:08
@File utils.py 
@Desciption
"""
import pandas as pd

def excelImport(excelfilename):
    """
    导入excel文件，并将其解析为数据库可插入内容
    :param excelfilename: 
    :return: 
    """
    df = pd.read_excel(excelfilename)
    text_data = []
    for i in df.index.values:
        row_data = df.ix[i,['故障现象', '故障原因', '故障处理']].to_dict()
        text_data.append(row_data)
    return text_data