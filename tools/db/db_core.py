#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2021/04/25 13:21
# FileName: db_core
# Description: 
# Question:

from tools.common.const import DB_HOST, DB_NAME, DB_PORT, DB_USER, DB_PASSWORD
from tools.logger import logger

import pymysql


# 数据库连接参数
db_host = DB_HOST
db_port = DB_PORT
db_user = DB_USER
db_password = DB_PASSWORD
db_name = DB_NAME


# 初始化日志
logger.init_logger()


def connect():
    # 连接数据库
    try:
        db = pymysql.connect(host=db_host, port=db_port, user=db_user, password=db_password, db=db_name)
        return db
    except Exception as e:
        logger.error(str(e))
        logger.error("Database connect failed, please chech the database configuration.")
        exit()


def search_wechat_account_is_existed(official_account_name):
    # 使用 cursor() 方法创建一个游标对象 cursor
    db = connect()
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT id FROM wechat_account_list \
           WHERE official_account_name = '{}'".format(official_account_name)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 关闭MySQLClient
        official_account_info = cursor.fetchall()
        cursor.close()
        db.close()
        return official_account_info[0][0] if len(official_account_info) != 0 else None
    except:
        logger.info("Do not find the official account in database, now starting to build a account map.")
    #    official_account_id = insert_wechat_account(official_account_name)
    #     return official_account_id


def insert_wechat_account(official_account_name):
    # 使用 cursor() 方法创建一个游标对象 cursor
    db = connect()
    cursor = db.cursor()
    # SQL 查询语句
    sql = """INSERT INTO wechat_account_list (official_account_name) VALUES (%s)"""
    try:
        # 执行SQL语句
        cursor.execute(sql, (official_account_name))
        # 获取所有记录列表
        sql = "SELECT id FROM wechat_account_list \
                   WHERE  official_account_name = '{}'".format(official_account_name)
        cursor.execute(sql)
        db.commit()
        # 获取所有记录列表
        results = cursor.fetchall()
        cursor.close()
        db.close()
        official_account_id = results[0][0]
        return official_account_id
    except Exception as e:
        db.rollback()  # 发生错误时回滚
        logger.error(str(e))
        logger.warning("Failed to add a official account.")
        return False


def insert_account_passage_link(title, passage_link, official_account_id):
    # 使用 cursor() 方法创建一个游标对象 cursor
    db = connect()
    cursor = db.cursor()
    # SQL 查询语句
    sql = "INSERT INTO passage_link_list(title, passage_link, official_account_id) select '{}', '{}', '{}' from DUAL where not exists (select title, passage_link, official_account_id from passage_link_list where passage_link = '{}')".format(title, passage_link, official_account_id, passage_link)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        db.commit()
        # 获取所有记录列表
        cursor.close()
        db.close()
    except Exception as e:
        db.rollback()  # 发生错误时回滚
        db.close()
        logger.error(str(e))
        logger.warning("Failed to add a new passage.")
        return False


def search_one_account_passage_by_id(id):
    # 使用 cursor() 方法创建一个游标对象 cursor
    db = connect()
    cursor = db.cursor()
    # mc = MysqlClient()
    # SQL 查询语句
    sql = "SELECT title, passage_link, official_account_id FROM passage_link_list \
              WHERE  official_account_id = '{}'".format(id)
    try:
        # results = mc.select_many(sql)
        # 获取所有记录列表
        cursor.execute(sql)
        results = cursor.fetchall()
        for i in range(len(results)):
           print(results[i])
        # return json.dumps(results[1], ensure_ascii=False)
        cursor.close()
        db.close()
        return results
    except Exception as e:
        db.rollback()  # 发生错误时回滚
        # mc.end()
        logger.error(str(e))
        logger.warning("Failed to search the history passage.")
        return False


if __name__ == '__main__':
    db = connect()
    cursor = db.cursor()
    cursor.close()
    cursor.close()