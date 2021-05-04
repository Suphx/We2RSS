#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2021/04/25 13:21
# FileName: db_core
# Description: 
# Question:

from tools.logger import logger
import pymysql

# 数据库连接参数
db_host = 'localhost'
db_port = 3306
db_user = 'root'
db_password = '123456'
db_name = 'wechat_official_account_passage_rss'


# 初始化日志
logger.init_logger()


# 连接数据库
try:
    db = pymysql.connect(host=db_host, port=db_port, user=db_user, password=db_password, db=db_name)
except Exception as e:
    logger.error(str(e))
    logger.error("数据库连接失败，请检查数据库连接参数配置情况。")
    exit()


def search_wechat_account_is_existed(official_account_name):
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT id FROM wechat_account_list \
           WHERE official_account_name = '{}'".format(official_account_name)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        official_account_id = results[0][0]
        return official_account_id
    except:
        logger.info("没有查询到对应公众号，将新建公众号映射。")
        official_account_id = insert_wechat_account(official_account_name)
        return official_account_id


def insert_wechat_account(official_account_name):
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = """INSERT INTO wechat_account_list (official_account_name) VALUES (%s)"""
    try:
        # 执行SQL语句
        cursor.execute(sql, (official_account_name))
        # 获取所有记录列表
        db.commit()
        sql = "SELECT id FROM wechat_account_list \
                   WHERE  official_account_name = '{}'".format(official_account_name)
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        official_account_id = results[0][0]
        return official_account_id
    except Exception as e:
        db.rollback()  # 发生错误时回滚
        logger.error(str(e))
        logger.warning("新增公众号失败。")
        return False


def insert_account_passage_link(title, passage_link, official_account_id):
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "INSERT INTO passage_link_list(title, passage_link, official_account_id) select '{}', '{}', '{}' from DUAL where not exists (select title, passage_link, official_account_id from passage_link_list where passage_link = '{}')".format(title, passage_link, official_account_id, passage_link)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        db.commit()
    except Exception as e:
        db.rollback()  # 发生错误时回滚
        logger.error(str(e))
        logger.warning("新增公众号推文失败。")
        return False


def search_one_account_passage_by_id(id):
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT title, passage_link, official_account_id FROM passage_link_list \
              WHERE  official_account_id = '{}'".format(id)
    try:
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for i in range(len(results)):
            print(results[i])
        return results
    except Exception as e:
        db.rollback()  # 发生错误时回滚
        logger.error(str(e))
        logger.warning("查询历史推文失败。")
        return False


if __name__ == '__main__':
    insert_account_passage_link("1","1",1)