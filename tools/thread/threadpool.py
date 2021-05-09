# -*- coding: utf-8 -*-
# @Time : 2021/5/9 21:14
# @Author : SuphxLin
# @Email : kiols6@aliyun.com
# @File : threadpool.py
# @Project : We2RSS
# @Description:

from concurrent.futures import ThreadPoolExecutor
from tools.core.request_history_article import get_lastest_history_passage

def thread_runner(thread_num, func, *args):
    executor = ThreadPoolExecutor(thread_num)
    executor.submit(get_lastest_history_passage, *args)
