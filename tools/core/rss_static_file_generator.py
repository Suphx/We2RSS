#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2021/04/25 13:21
# FileName: passage_link_gen_rss
# Description: 
# Question:

import datetime
import PyRSS2Gen
import os


def generate_rss_item(passage_title, passage_link, passage_value):
    rss_item = PyRSS2Gen.RSSItem(
        title = passage_title,
        link = passage_link,
        description = passage_value,
        pubDate = datetime.datetime.now())
    return rss_item


def gen_rss(description, subscriber, *rssitems, output_dir):
    rss = PyRSS2Gen.RSS2(
       title = subscriber + "微信公众号订阅内容",
       link = "http://rss.suphxlin-tech.com",
       description = description,
       lastBuildDate = datetime.datetime.now(),
       items=rssitems
    )
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    rss.write_xml(open(os.path.join(output_dir, subscriber+".xml"), "w+", encoding='utf-8'))