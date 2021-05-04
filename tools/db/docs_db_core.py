# -*- coding: utf-8 -*-
# @Time : 2021/5/3 15:03
# @Author : SuphxLin
# @Email : kiols6@aliyun.com
# @File : docs_db_core.py
# @Project : We2RSS
# @Description:

from tools.logger import logger
import pymongo

DB_NAME = "we2rss"
DB_URL = "localhost"
COL_NAME = "passage_collections"

def build_db_col_session(db_name, col_name, db_url, port=27017):
    mongodb_client = pymongo.MongoClient("mongodb://{}:{}/".format(db_url, port))
    mongodb_instance = mongodb_client[db_name]
    collection_session = mongodb_instance[col_name]
    return collection_session


def insert_docs(docs_list, passage_title, col_name=COL_NAME):
    col_session = build_db_col_session(DB_NAME, col_name, DB_URL)
    try:
        filter_name = {"passage_title": passage_title}
        col_session.update_many(filter=filter_name, update=docs_list, upsert=True)
    except Exception as e:
        logger.error(str(e))
        logger.error("新增文档失败。")
        print(str(e))
        print("新增文档失败。")


def find_docs(query, col_name):
    col_session = build_db_col_session(DB_NAME, col_name, DB_URL)
    try:
        find_doc = col_session.find(query)
        return find_doc
    except Exception as e:
        logger.error(str(e))
        logger.error("查询失败。")
        print(str(e))
        print("查询失败。")


if __name__ == '__main__':
    docs = {"official_account_id": 1, "passage_title": 1, "passage_link": 1,
            "passage_create_time": 1,
            "passage_update_time": 1}
    docs_mongo = {"$set": docs}
    insert_docs(docs_mongo, "passage_collections")  # MongoDB数据库更新