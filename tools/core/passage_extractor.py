# -*- coding: utf-8 -*-
# @Time : 2021/5/3 11:02
# @Author : SuphxLin
# @Email : kiols6@aliyun.com
# @File : passage_extractor.py
# @Project : We2RSS
# @Description:

from tools.db.oss_core import download_img, upload_file
from tools.db.docs_db_core import insert_file_into_gridfs
from tools.common.utils import generate_filename
from tools.common.const import OUTPUT_ROOT_DIR

import requests
from bs4 import BeautifulSoup

import os
import re


def resolve_passage_from_url(passage_url, official_account_name):
    response = requests.get(passage_url)
    response.encoding = "utf_8"
    result = response.content # 链接全信息
    passage_uuid = generate_filename()
    '''
    需在此修改：
    解析后，图片、视频、音频、CSS等需要换外链
    '''
    bs = BeautifulSoup(result, 'html.parser', from_encoding='utf8')
    # 文章css
    style = bs.find('style')  # 文章美化js

    # 逐级解析推文
    js_article = bs.find('div', id='js_article', class_='rich_media')
    # official_account_name = js_article.find('a', id='js_name').string.strip()
    rich_media_inner = js_article.find('div', class_='rich_media_inner')
    title = rich_media_inner.find('h2', class_='rich_media_title').string.strip()  # 文章标题
    title = re.sub(r'[\\\\/:*?\"<>|]', '', title)  # 正则处理文件名，避免文件无法创建
    js_article.find('div', class_='rich_media_content').attrs['style'] = 'visibility: show;'  # 文章内容设置可见

    # 处理图片，替换外链
    img_list = js_article.find_all('img')
    for img_tag in img_list:
        if img_tag.has_attr('data-src'):
            localfile, img_filename = download_img(img_tag.attrs['data-src'], official_account_name, passage_uuid, img_tag.attrs['data-type'])
            oss_path = upload_file(localfile, '{}/{}'.format("image", img_filename))
            insert_file_into_gridfs(localfile)
            img_tag.attrs['src'] = oss_path

    output_html = """
    <html>
    <head>
    <title>{}</title>
    <meta charset="utf-8">
    {}
    </head>
    <body>
    {}
    </body>
    </html>
    """.format(title, style, js_article)
    f = open(os.path.join(OUTPUT_ROOT_DIR, official_account_name, '{}.html'.format(title)), mode='w', encoding='utf8')
    f.write(output_html)
    f.close()
    insert_file_into_gridfs(os.path.join(OUTPUT_ROOT_DIR, official_account_name, '{}.html'.format(title)))
    return output_html


if __name__ == '__main__':
    pass