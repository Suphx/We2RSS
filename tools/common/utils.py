# -*- coding: utf-8 -*-
# @Time : 2021/5/15 19:34
# @Author : SuphxLin
# @Email : kiols6@aliyun.com
# @File : utils.py
# @Project : We2RSS
# @Description:

import uuid


def generate_filename():
    uid = str(uuid.uuid4())
    return ''.join(uid.split('-'))