# -*- coding: utf-8 -*-
# @Time : 2021/5/3 11:02
# @Author : SuphxLin
# @Email : kiols6@aliyun.com
# @File : passage_extractor.py
# @Project : We2RSS
# @Description:

import requests
from bs4 import BeautifulSoup
from tools.db.oss_core import download_img, upload_file
from tools.common.utils import generate_filename

def resolve_passage_from_url(passage_url):
    response = requests.get(passage_url)
    response.encoding = "utf_8"
    result = response.content # 链接全信息
    passage_uuid = generate_filename()
    '''
    需在此修改：
    解析，图片、视频、音频等需要换外链
    '''
    bs = BeautifulSoup(result, 'html.parser', from_encoding='utf8')
    # 文章css
    style = bs.find('style')  # 文章美化js

    # 逐级解析推文
    js_article = bs.find('div', id='js_article', class_='rich_media')
    official_account_name = js_article.find('a', id='js_name').string.strip()
    rich_media_inner = js_article.find('div', class_='rich_media_inner')
    title = rich_media_inner.find('h2', class_='rich_media_title').string.strip()  # 文章标题

    js_article.find('div', class_='rich_media_content').attrs['style'] = 'visibility: show;'  # 文章内容设置可见
    # 处理图片，替换外链
    img_list = js_article.find_all('img')
    for img_tag in img_list:
        if img_tag.has_attr('data-src'):
            localfile, img_filename = download_img(img_tag.attrs['data-src'], official_account_name, passage_uuid, img_tag.attrs['data-type'])
            oss_path = upload_file(localfile, '{}/{}'.format("image", img_filename))
            img_tag.attrs['src'] = oss_path


    # is_original = rich_media_inner.find('span', id='copyright_logo').string.strip()  # 是否原创

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
    return output_html


if __name__ == '__main__':
    html_content = str(resolve_passage_from_url("https://mp.weixin.qq.com/s?__biz=MzA3MTM4Mzk0OQ==&mid=2670429416&idx=1&sn=c759306da07e97a64f1d5f2f40d24af6&chksm=85f14a0ab286c31ce1aae31e2d8e95df4e232d90dc08b4aaf50402ad20a2c6ca4fb88994872d#rd"))
    f = open('test.html', 'w', encoding='utf8')
    f.write(html_content)
    f.close()