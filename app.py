# -*- coding: utf-8 -*-
# @Time : 2021/5/9 21:18
# @Author : SuphxLin
# @Email : kiols6@aliyun.com
# @File : app.py
# @Project : We2RSS
# @Description:

from tools.thread.threadpool import thread_runner
from tools.core.request_history_article import get_lastest_history_passage
from tools.logger import logger


from flask_cors import CORS
from flask import Flask, request, send_file, jsonify
from flask_restful import reqparse

# 初始化日志
logger.init_logger()

app = Flask(__name__)
CORS(app)


@app.route('/api/v1/getHistoryPassages', methods=['POST'])
def do_get_history_passages_api():
    args = reqparse.RequestParser(). \
        add_argument('OfficialAccountName', type=str). \
        parse_args()
    official_account_name = args['OfficialAccountName']
    try:
        thread_runner(1, get_lastest_history_passage, official_account_name)
        # get_lastest_history_passage(official_account_name)
        print("启动新线程开始爬取{}公众号".format(official_account_name))
        return "启动新线程开始爬取{}公众号".format(official_account_name)
    except Exception as e:
        print(str(e))
        logger.error(str(e))
        return "Error with {}".format(e)

if __name__ == "__main__":
    app.run(host="192.168.50.241", port=8443, debug=True)