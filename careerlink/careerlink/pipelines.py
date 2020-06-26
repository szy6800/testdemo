# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib

import requests


class CareerlinkPipeline(object):

    def process_item(self, item, spider):
        # url = 'http://54.169.251.189/enterprise/Job_Controller/addJob'
        url = 'https://fastjob.work/index.php/enterprise/Job_Controller/addJob'
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        datas = item


        res = requests.post(url, data=datas, headers=headers).text
        print('****************************************************')
        print(datas)
        print(res)
