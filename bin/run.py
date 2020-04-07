#!/usr/bin/env python
# encoding: utf-8
'''
@author:chenzhimin
@software:APITest
@file:run.py
@time:2020/4/3  10:44
@desc
'''
import unittest
from BeautifulReport import BeautifulReport
from model.setting import *




file_name = '{}接口测试.html'.format(TIME)
#选择要执行的用例
discover =unittest.defaultTestLoader.discover(CASE_PATH,'test*.py')

BeautifulReport(discover).report(description='接口测试',filename=file_name,report_dir=REPORT_PATH)