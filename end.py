# -*- coding:utf-8 -*-
"""
@author liuning
@date 2019/6/16 14:05
@File end.py.py 
@Desciption
"""
from app import create_app
app = create_app()
#
# @app.shell_context_processor
# def make_shell_context():
#     return {'db':db,'User':User,'History':History}
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)