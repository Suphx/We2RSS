#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2021/04/25 13:21
# FileName: passage_link_gen_rss
# Description: 
# Question:

from tools.db.docs_db_core import find_docs
from tools.db.db_core import search_wechat_account_is_existed
from tools.db.oss_core import upload_file, flush_resource
from tools.core.passage_extractor import resolve_passage_from_url
from tools.common.const import OUTPUT_ROOT_DIR
from tools.cache.localcache import update_log

import PyRSS2Gen

import os
import datetime
import time


def generate_subscribe_rss(official_account_name):
    if official_account_name in update_log:
        if update_log[official_account_name] == time.strftime('%Y-%m-%d',time.localtime(time.time())):
            return
    else:
        official_account_id= search_wechat_account_is_existed(official_account_name)
        query = {'official_account_id':official_account_id}
        result = list(find_docs(query))[:8]
        rss_items_list = list()
        for doc in result:
            passage_title = doc['passage_title']
            passage_link = doc['passage_link']
            description = resolve_passage_from_url(passage_link, official_account_name)
            rss_item = generate_rss_item(passage_title, passage_link, description)
            rss_items_list.append(rss_item)
        if len(result) != 0:
            rss_file_path = gen_rss(official_account_name, rss_items_list, os.path.join(OUTPUT_ROOT_DIR,'rss'))
            res_url = upload_file(rss_file_path, "{}/{}.xml".format('rss_service', official_account_name))
            flush_resource(res_url)
            update_log[official_account_name] = time.strftime('%Y-%m-%d', time.localtime(time.time()))


def generate_rss_item(passage_title, passage_link, passage_value):
    rss_item = PyRSS2Gen.RSSItem(
        title = passage_title,
        link = passage_link,
        description = passage_value,
        pubDate = datetime.datetime.now())
    return rss_item


def gen_rss(subscriber, rssitems, output_dir):
    rss = PyRSS2Gen.RSS2(
       title = subscriber + "微信公众号订阅内容",
       link = "http://rss.suphxlin-tech.com",
       description = subscriber + "微信公众号订阅内容",
       lastBuildDate = datetime.datetime.now(),
       items=rssitems
    )
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    rss.write_xml(open(os.path.join(output_dir, subscriber+".xml"), "w+", encoding='utf-8'))
    return os.path.join(output_dir, subscriber+".xml")


if __name__ == '__main__':
    pass