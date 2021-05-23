# -*- coding: utf-8 -*-
# @Time : 2021/5/9 21:18
# @Author : SuphxLin
# @Email : kiols6@aliyun.com
# @File : app.py
# @Project : We2RSS
# @Description:

from tools.thread.threadpool import thread_runner
from tools.core.request_history_article import get_lastest_history_passage
from tools.core.rss_static_file_generator import generate_subscribe_rss
from tools.db.db_core import search_wechat_account_is_existed, insert_wechat_account
from tools.db.docs_db_core import count_docs_exist, find_docs
from tools.logger import logger
from tools.common.const import CDN_ROOT

from flask_cors import CORS
from flask import Flask
from flask_restful import reqparse

# 初始化日志
logger.init_logger()

app = Flask(__name__)
CORS(app)


@app.route('/api/v1/isExist', methods=['POST'])
def do_get_is_exist_official_account():
    args = reqparse.RequestParser(). \
        add_argument('OfficialAccountName', type=str). \
        parse_args()
    official_account_name = args['OfficialAccountName']
    result = search_wechat_account_is_existed(official_account_name)
    return {'is_exist':str(False) if result is None else str(True)}


@app.route('/api/v1/getHistoryPassages', methods=['POST'])
def do_get_history_passages_api():
    args = reqparse.RequestParser(). \
        add_argument('OfficialAccountName', type=str). \
        parse_args()
    official_account_name = args['OfficialAccountName']
    is_existed = search_wechat_account_is_existed(official_account_name)
    if is_existed is None:
        insert_wechat_account(official_account_name)
    try:
        thread_runner(1, get_lastest_history_passage, official_account_name)
        # get_lastest_history_passage(official_account_name)
        print("启动新线程开始爬取{}公众号".format(official_account_name))
        return "启动新线程开始爬取{}公众号".format(official_account_name)
    except Exception as e:
        print(str(e))
        logger.error(str(e))
        return


@app.route('/api/v1/generateRss', methods=['POST'])
def do_generate_rss_api():
    args = reqparse.RequestParser(). \
        add_argument('OfficialAccountName', type=str). \
        parse_args()
    official_account_name = args['OfficialAccountName']
    generate_subscribe_rss(official_account_name)
    # thread_runner(1, generate_subscribe_rss, official_account_name)
    return "{}rss_service/{}.xml".format(CDN_ROOT, official_account_name)


@app.route('/api/v1/statistics', methods=['GET'])
def do_generate_statistic_api():
    result = count_docs_exist()
    message_head = "累计收录推文统计:\n"
    message = list()
    result = list(result)
    for sta in result:
        mes = "{}:{}篇".format(sta['official_account_name'][0], sta['count'])
        message.append(mes)
    mess = "\n".join(message)
    return message_head + mess


@app.route('/api/v1/searchPassage', methods=['POST'])
def do_search_history_passage_api():
    args = reqparse.RequestParser(). \
        add_argument('PassageTitle', type=str). \
        parse_args()
    PassageTitle = args['PassageTitle']
    # query = {"passage_title": {"$regex": PassageTitle}}
    query = {"$text": {"$search": PassageTitle}}
    result = find_docs(query)
    result = list(result)[:5]
    his_passage = {}
    for res in result:
        his_passage[res['passage_title']] = res['passage_link']
    return his_passage


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8443, debug=True)