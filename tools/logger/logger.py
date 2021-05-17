#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2021/04/25 13:24
# FileName: logger
# Description: 
# Question:

from tools.common.const import LOGGER_DIR

import logging
import os
import datetime


# 初始化日志
def init_logger():
    # 初始化日志存放位置
    if not os.path.exists(LOGGER_DIR):
        os.makedirs(LOGGER_DIR)
    # 初始化日志格式
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    date_format = "%Y/%m/%d %H:%M:%S %p"
    # 初始化日志配置
    logging.basicConfig(filename="{}/{}.txt".format(LOGGER_DIR, str(datetime.date.today())), level=logging.DEBUG, format=log_format,
                        datefmt=date_format)


def info(msg):
    logging.info(msg)


def warning(msg):
    logging.warning(msg)


def debug(msg):
    logging.debug(msg)


def error(msg):
    logging.error(msg)