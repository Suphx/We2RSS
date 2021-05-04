#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2021/04/25 13:21
# FileName: request_history_article
# Description: 
# Question:

import requests
import json
import re
import random
import time
import logging
from tools.logger import logger
from tools.db import db_core, docs_db_core
from dateutil import parser
import datetime

logger.init_logger()


def time_format(timestamp):
    date_array = datetime.datetime.fromtimestamp(timestamp)
    other_style_time = date_array.strftime("%Y-%m-%d %H:%M:%S")
    date_time = parser.parse(other_style_time)
    return date_time


def get_lastest_history_passage(query):
    # query为要爬取的公众号名称
    # 公众号主页
    url = 'https://mp.weixin.qq.com'
    # 设置headers
    header = {
        "HOST": "mp.weixin.qq.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3239.132"
    }
    from requests.packages import urllib3
    urllib3.disable_warnings()  # 关闭警告

    # 读取登陆成功后获取到的cookies
    with open('../../cookies.txt', 'r', encoding='utf-8') as f:
        cookie = f.read()
    cookies = json.loads(cookie)
    # 增加重试连接次数
    session = requests.Session()
    session.keep_alive = False
    # 增加重试连接次数
    session.adapters.DEFAULT_RETRIES = 511

    # 登录之后的微信公众号首页url变化为：https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=1849751598，从这里获取token信息
    response = session.get(url=url, cookies=cookies, verify=False)
    token = re.findall(r'token=(\d+)', str(response.url))[0]
    time.sleep(15)
    # 搜索微信公众号的接口地址
    search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
    # 搜索微信公众号接口需要传入的参数，有三个变量：微信公众号token、随机数random、搜索的微信公众号名字
    query_id = {
        'action': 'search_biz',
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'query': query,
        'begin': '0',
        'count': '5'
    }
    # 打开搜索微信公众号接口地址，需要传入相关参数信息如：cookies、params、headers
    search_response = session.get(
        search_url,
        cookies=cookies,
        headers=header,
        params=query_id)
    # 取搜索结果中的第一个公众号
    lists = search_response.json().get('list')
    logging.info("查询到公众号信息列表：" + str(lists))
    # 获取这个公众号的fakeid，后面爬取公众号文章需要此字段
    fakeid = lists[0].get('fakeid')
    # 微信公众号文章接口地址
    appmsg_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'
    # 搜索文章需要传入几个参数：登录的公众号token、要爬取文章的公众号fakeid、随机数random
    query_id_data = {
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'action': 'list_ex',
        'begin': '0',  # 不同页，此参数变化，变化规则为每页加5
        'count': '5',
        'query': '',
        'fakeid': fakeid,
        'type': '9'
    }
    # 打开搜索的微信公众号文章列表页
    appmsg_response = session.get(
        appmsg_url,
        cookies=cookies,
        headers=header,
        params=query_id_data,
    )
    # 获取文章总数
    # max_num = appmsg_response.json().get('app_msg_cnt')
    # 只爬取最新
    # max_num = 10
    # 每页至少有5条，获取文章总的页数，爬取时需要分页爬
    # num = int(int(max_num) / 5)
    num = 2
    # 起始页begin参数，往后每页加5
    begin = 0

    # 获取公众号在MySQL数据库中的ID
    official_account_id = db_core.search_wechat_account_is_existed(query)
    # 开始爬取
    print("开始爬取！")
    while num + 1 > 0:
        query_id_data = {
            'token': token,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            'random': random.random(),
            'action': 'list_ex',
            'begin': '{}'.format(str(begin)),
            'count': '5',
            'query': '',
            'fakeid': fakeid,
            'type': '9'
        }
        print('正在翻页：--------------', begin)
        time.sleep(15)

        # 获取每一页文章的标题和链接地址，并写入本地文本中
        query_fakeid_response = requests.get(
            appmsg_url,
            cookies=cookies,
            headers=header,
            params=query_id_data,
            timeout=3)
        fakeid_list = query_fakeid_response.json().get('app_msg_list')
        if fakeid_list:
            for item in fakeid_list:
                content_link = item.get('link')                # 文章链接
                content_title = item.get('title')              # 文章标题
                content_create_time = item.get('create_time')  # 文章发布时间
                content_update_time = item.get('update_time')  # 文章更新时间
                # 组装MongoDB插入数据
                docs = {"passage_title": content_title, "official_account_id": official_account_id, "passage_link":content_link, "passage_create_time":time_format(content_create_time), "passage_update_time":time_format(content_update_time)}
                docs_mongo = {"$set":docs}

                db_core.insert_account_passage_link(content_title, content_link, official_account_id)  # MySQL数据库更新
                docs_db_core.insert_docs(docs_mongo, "passage_collections")                            # MongoDB数据库更新

        num -= 1
        begin = int(begin)
        begin += 5


if __name__ == '__main__':
    get_lastest_history_passage("南航青年志愿者")