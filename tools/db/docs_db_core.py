# -*- coding: utf-8 -*-
# @Time : 2021/5/3 15:03
# @Author : SuphxLin
# @Email : kiols6@aliyun.com
# @File : docs_db_core.py
# @Project : We2RSS
# @Description:

from tools.logger import logger
from tools.common.const import MONGODB_PORT, MONGODB_NAME, MONGODB_URL, MONGODB_COL_NAME
from tools.db.db_core import search_wechat_account

import pymongo
from gridfs import GridFS


DB_NAME = MONGODB_NAME
DB_URL = MONGODB_URL
COL_NAME = MONGODB_COL_NAME


def build_db_col_session(db_name, col_name, db_url, port=MONGODB_PORT):
    mongodb_client = pymongo.MongoClient("mongodb://{}:{}/".format(db_url, port))
    mongodb_instance = mongodb_client[db_name]
    collection_session = mongodb_instance[col_name]
    return mongodb_instance, collection_session


def insert_docs(docs_list, passage_link, col_name=COL_NAME):
    _, col_session = build_db_col_session(DB_NAME, col_name, DB_URL)
    try:
        filter_name = {"passage_link": passage_link}
        col_session.update_many(filter=filter_name, update=docs_list, upsert=True)
    except Exception as e:
        logger.error(str(e))
        logger.error("Failed to update passages。")
        print(str(e))
        print("Failed to update passages。")


def update_official_account_collections(col_name="wechat_account_collections"):
    _, col_session = build_db_col_session(DB_NAME, col_name, DB_URL)
    result = search_wechat_account()
    for res in result:
        docs = {"official_account_id":res[0], "official_account_name":res[1]}
        try:
            filter_name = {"official_account_id":res[0]}
            docs_list = {"$set":docs}
            col_session.update_many(filter=filter_name, update=docs_list, upsert=True)
        except Exception as e:
            logger.error(str(e))
            logger.error("Failed to update official account collections。")
            print(str(e))
            print("Failed to update official account collections。")


def insert_file_into_gridfs(file_name, col_name="we2rss_store"):
    mongodb_instance, _ = build_db_col_session(DB_NAME, col_name, DB_URL)
    gridfs_col = GridFS(mongodb_instance, collection=col_name)
    filter_condition = {"filename": file_name}
    with open("%s" % file_name, 'rb') as file:
        waited_for_store = file.read()
        file_ = gridfs_col.put(data=waited_for_store, **filter_condition)  # 上传到gridfs
        print(file_)


def find_docs(query, col_name=COL_NAME):
    _, col_session = build_db_col_session(DB_NAME, col_name, DB_URL)
    try:
        find_doc = col_session.find(query).sort([("passage_create_time", -1)])
        return find_doc
    except Exception as e:
        logger.error(str(e))
        logger.error("Failed to search passages.")
        print(str(e))
        print("Failed to search passages.")


def count_docs_exist(col_name=COL_NAME):
    update_official_account_collections()
    _, col_session = build_db_col_session(DB_NAME, col_name, DB_URL)
    try:
        find_doc = col_session.aggregate([{"$lookup":
                                               {"from": "wechat_account_collections",
                                                "localField": "official_account_id",
                                                "foreignField": "official_account_id",
                                                "as": "official_account"}},
                                          {"$group":
                                               {"_id": "$official_account", "count": {"$sum": 1}}},
                                          {"$project": {"_id": 0,
                                                        "official_account_name": "$_id.official_account_name",
                                                        "count": 1}},
                                          {"$sort": {"count": -1}}])
        return find_doc
    except Exception as e:
        logger.error(str(e))
        logger.error("Failed to count passages.")
        print(str(e))
        print("Failed to count passages.")


if __name__ == '__main__':
    # docs = {"official_account_id": 1, "passage_title": 1, "passage_link": 1,
    #         "passage_create_time": 1,
    #         "passage_update_time": 1}
    # docs_mongo = {"$set": docs}
    # insert_docs(docs_mongo, "passage_collections")  # MongoDB数据库更新
    # insert_file_into_gridfs(r"E:\PythonProject\We2RSS\README.md")
    query = {"passage_title": {"$regex": "图"}}
    result = find_docs(query, col_name=COL_NAME)
    result = list(result)
    his_passage = {}
    for res in result:
        his_passage[res['passage_title']] = res['passage_link']
    print(his_passage)