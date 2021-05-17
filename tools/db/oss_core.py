# -*- coding: utf-8 -*-
# @Time : 2021/5/3 15:26
# @Author : SuphxLin
# @Email : kiols6@aliyun.com
# @File : oss_core.py
# @Project : We2RSS
# @Description:

from tools.common import utils
from tools.common.const import ACCESS_KEY, SECRET_KEY, BUCKET_NAME, CDN_ROOT, OUTPUT_ROOT_DIR
from qiniu import Auth, put_file, etag, CdnManager

import requests
import os

# 需要填写你的 Access Key 和 Secret Key
access_key = ACCESS_KEY
secret_key = SECRET_KEY
# 构建鉴权对象
q = Auth(access_key, secret_key)
# 要上传的空间
bucket_name = BUCKET_NAME
# 本地缓存
img_tmp_dir = OUTPUT_ROOT_DIR
# cdn根路径
cdn_root = CDN_ROOT


def download_img(img_url, official_account_name, passage_title, img_type):
    '''
    :param img_url: 图片链接
    :param official_account_name: 公众号名称
    :param passage_title: 文章标题
    :param img_type: 图片类型
    :return: 下载图片的完整路径
    '''
    local_img_filename = utils.generate_filename()
    local_img_path = os.path.join(img_tmp_dir, official_account_name, passage_title, img_type)
    if not os.path.exists(local_img_path):
        os.makedirs(local_img_path)
    r = requests.get(img_url)
    if r.status_code == 200:
        f = open(os.path.join(local_img_path, "{}.{}".format(local_img_filename, img_type)), 'wb')
        f.write(r.content)  # 将内容写入图片
        f.close()
    return os.path.join(local_img_path, "{}.{}".format(local_img_filename, img_type)), "{}.{}".format(local_img_filename, img_type)


def upload_file(localfile, key):
    '''
    :param localfile:  本地图片路径
    :param key: 上传到OSS上的名称
    :return: CDN路径
    '''
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    ret, info = put_file(token, key, localfile)
    # print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)
    return cdn_root + key


def flush_resource(url):
    cdn_manager = CdnManager(q)
    # 需要刷新的文件链接
    urls = [
        url
    ]
    # 刷新链接
    refresh_url_result = cdn_manager.refresh_urls(urls)
    print(refresh_url_result)


if __name__ == '__main__':
    flush_resource('http://rss.suphxlin-tech.com/rss_service/CodeSheep.xml')
    # download_img('https://mmbiz.qpic.cn/mmbiz_jpg/lJxjkdq8Pqo4lXCg5VhETicg6AicouR5FntfDj0tgrQAUPAJlibWCLzgI89CY7FpDKn3ibTLufOEMwlaWIiaPY6iayJQ/640?wx_fmt=jpeg', 'jpeg')