# -*- coding: utf-8 -*-
# @Time : 2021/5/20 18:40
# @Author : SuphxLin
# @Email : kiols6@aliyun.com
# @File : update_passage_repo.py
# @Project : We2RSS
# @Description:

from tools.db.db_core import search_wechat_account
from tools.core.request_history_article import get_lastest_history_passage

import time


def update_repo():
    official_account_list = search_wechat_account()
    for official_account in official_account_list:
        official_account_name = official_account[1]
        get_lastest_history_passage(official_account_name)
        print("{}公众号更新完成，进入600秒冷却时间。".format(official_account_name))
        time.sleep(600)


if __name__ == '__main__':
    update_repo()