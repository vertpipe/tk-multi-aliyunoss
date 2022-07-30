#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author : reliable-天
# @Contact : U{johnny.zxt@gmail.com<johnny.zxt@gmail.com>}
# @Website : http://zxto.top:1580
# @Gitlab  : http://zxto.top:30000
# @Time : 2022/7/9 15:04
# @File : aliyun_osstest.py
# @Description :

import os
import sys
# prj_folder = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # get the folder tk-multi-aliyunoss prject
# py_pkg = '{}/python/py_package'.format(prj_folder)
# sys.path.append(py_pkg)
from ..py_package import oss2

endpoint = 'https://oss-cn-shanghai.aliyuncs.com'  # 假设你的Bucket处于shanghai区域

auth = oss2.Auth('LTAI5t8ea1fFZgH82PEYU7RS', 'KJlwYVjlfyTMWv6bBdFxHZ3k57tJxA')
bucket = oss2.Bucket(auth, endpoint, 'vertpipeshotgrid')
# https://vertpipeshotgrid.oss-cn-shanghai.aliyuncs.com/story.txt?OSSAccessKeyId=LTAI5t8ea1fFZgH82PEYU7RS&Expires=1656082319&Signature=smUuDevbf3UlFlUZytFhx9onBLQ%3D
# Bucket中的文件名（key）为story.txt

def oss_upload(local_filepath, remote_filepath):
    bucket.put_object_from_file(remote_filepath, local_filepath)

if __name__ == '__main__':
    lo_fp = '/Users/johnnyzxt/temp/mycar.ma'
    re_fp = 'test/mycar.ma'
    oss_upload(lo_fp, re_fp)





