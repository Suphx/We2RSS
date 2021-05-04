# -*- coding: utf-8 -*-
# @Time : 2021/5/3 11:02
# @Author : SuphxLin
# @Email : kiols6@aliyun.com
# @File : passage_extractor.py
# @Project : We2RSS
# @Description:

import requests


def resolve_passage_from_url(passage_url):
    response = requests.get(passage_url)
    response.encoding = "utf_8"
    result = response.text # 链接全信息
    '''
    需在此修改：
    解析，图片、视频、音频等需要换外链
    '''
    return result

