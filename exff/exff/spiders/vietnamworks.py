# -*- coding: utf-8 -*-
import datetime
import json
import re
import time
from copy import deepcopy

import jsonpath
import scrapy

from exff.items import ExffItem


class AaSpider(scrapy.Spider):
    name = 'vietnamworks'
    allowed_domains = ['vietnamworks.com']
    start_urls = ['http://vietnamworks.com/']

    def start_requests(self):
        #循环135页
        for i in range(0,10):
        #构建post请求参数
            data = {"requests": [{"indexName": "vnw_job_v2_35",
                                  "params": "query=java&query=java&facetFilters=%5B%5B%22categoryIds%3A35%22%5D%5D&filters=&numericFilters=%5B%5D&page={}&hitsPerPage=50&restrictSearchableAttributes=%5B%22jobTitle%22%2C%22skills%22%2C%22company%22%5D&attributesToRetrieve=%5B%22*%22%2C%22-jobRequirement%22%2C%22-jobDescription%22%5D&attributesToHighlight=%5B%5D".format(i)}]}
        #发送post请求
            yield scrapy.FormRequest(
                url = 'http://jf8q26wwud-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser&x-algolia-application-id=JF8Q26WWUD&x-algolia-api-key=2bc790c0d4f44db9ab6267a597d17f1a',
                method='POST',
                body=json.dumps(data),
                headers={'Content-Type': 'application/json'},
                callback = self.parse)
#获取列表页url
    def parse(self, response):
        item = ExffItem()
        text = json.loads(response.text)
        alias = jsonpath.jsonpath(text, '$..alias')
        jobid = jsonpath.jsonpath(text, '$..jobId')
        for i,b in zip(alias,jobid):
            item['src_url'] = 'https://www.vietnamworks.com/' + i + '-' + str(b) + '-jd'
            yield scrapy.Request(item['src_url'], callback=self.parse_info2, meta={'item': deepcopy(item)},
                                 dont_filter=True)

    def parse_info2(self, response):
        # 传参数
        item = response.meta['item']
        # 职位名称
        item['name'] = response.xpath('//*[@class="job-title"]/text()').get().strip()
        # 发布人
        item['creator'] = ''
        # 工作类型1-全职,2-兼职,3-实习',
        item['work_type'] = 1
        # 工资类型1-月薪，2-周薪，3-日薪',
        item['salary_type'] = 1
        # 最小薪资
        try:
            min_salary = response.xpath('//*[@class="salary"]/strong/text()').get().strip()
            if min_salary == 'Negotiable':
                item['min_salary'] = ''
            else:
                # min_salary1 = min_salary.split(' - ')[0]
                item['min_salary'] = re.findall('\d+', min_salary)[0]

            # 最大薪资

            max_salary = response.xpath('//*[@class="salary"]/strong/text()').get().strip()
            if max_salary == 'Negotiable':
                item['max_salary'] = ''
            else:
                item['max_salary'] = re.findall('\d+', max_salary)[1]
        except:
            pass
        # 货币
        item['currency'] = 'USD'
        # 行业
        industry = response.xpath('//*[@class="col-xs-10 summary-content"]/span/a/text()').getall()
        sss = ''
        for i in industry:
            sss = sss + i.strip() + "||"
        item['industry'] = sss

        # 学历要求
        edu_level = ''.join(response.xpath('//*[@class="col-md-8  col-sm-12 tab-main-content"]/div[3]/div/text()').getall())
        # 不限学历
        if 'Không yêu cầu' in edu_level:
            item['edu_level'] = 0
            # 高中
        elif 'Trung cấp' in edu_level:
            item['edu_level'] = 1
        elif 'Trung cấp trở lên' in edu_level:
            item['edu_level'] = 1
            # 大学专科
        elif 'Bachelor / Technical degrees' in edu_level:
            item['edu_level'] = 2
        elif 'Colleague' in edu_level:
            item['edu_level'] = 2
        elif 'Đại học' in edu_level:
            item['edu_level'] = 2
        elif 'Đại học trở lên' in edu_level:
            item['edu_level'] = 2
            # 大学本科
        elif 'Cao đẳng' in edu_level:
            item['edu_level'] = 2
        elif 'Cao đẳng trở lên' in edu_level:
            item['edu_level'] = 2
            # 研究生
        elif 'bác sĩ' in edu_level:
            item['edu_level'] = 3
        elif 'bác sĩ trở lên' in edu_level:
            item['edu_level'] = 3
            # 博士
        elif 'tiến sĩ' in edu_level:
            item['edu_level'] = 4
        elif 'tiến sĩ trở lên' in edu_level:
            item['edu_level'] = 4
        else:
            item['edu_level'] = 0
        # 国家
        item['country'] = 'VN'
        # 城市
        city = response.xpath('//*[@itemprop="address"]/text()').get()
        if city == 'Ho Chi Minh':
            item['city'] = 1
        elif city == 'Ha Noi':
            item['city'] = 2
        elif city == 'An Giang':
            item['city'] = 3
        elif city == 'Bac Lieu':
            item['city'] = 4
        elif city == 'Ba Ria-Vung Tau':
            item['city'] = 5
        elif city == 'Bac Cạn':
            item['city'] = 6
        elif city == 'Bac Giang':
            item['city'] = 7
        elif city == 'Bac Ninh':
            item['city'] = 8
        elif city == 'Ben Tre':
            item['city'] = 9
        elif city == 'Binh Diong':
            item['city'] = 10
        elif city == 'Binh Dinh':
            item['city'] = 11
        elif city == 'Binh Phuoc':
            item['city'] = 12
        elif city == 'Binh Thuan':
            item['city'] = 13
        elif city == 'Cao Bang':
            item['city'] = 14
        elif city == 'Ca Mau':
            item['city'] = 15
        elif city == 'Can Tho':
            item['city'] = 16
        elif city == 'Da Nang':
            item['city'] = 17
        elif city == 'Dak Lak':
            item['city'] = 18
        elif city == 'Dak Nong':
            item['city'] = 19
        if city == 'Dien Bien':
            item['city'] = 20
        if city == 'Dong Nai':
            item['city'] = 21
        if city == 'Dong Thap':
            item['city'] = 22
        if city == 'Gia Lai':
            item['city'] = 23
        if city == 'Ha Giang':
            item['city'] = 24
        if city == 'Ha Nam':
            item['city'] = 25
        if city == 'Ha Tinh':
            item['city'] = 27
        if city == 'Hai Duong':
            item['city'] = 28
        if city == 'Hai Phong':
            item['city'] = 29
        if city == 'Hau Giang':
            item['city'] = 30
        if city == 'Hoa Binh':
            item['city'] = 31
        if city == 'Hung Yen':
            item['city'] = 32
        if city == 'Khanh Hoa':
            item['city'] = 33
        if city == 'Kien Giang':
            item['city'] = 34
        if city == 'Kon Tum':
            item['city'] = 35
        if city == 'Lai Chau':
            item['city'] = 36
        if city == 'Lang Son':
            item['city'] = 37
        if city == 'Lào Cai':
            item['city'] = 38
        if city == 'Lam Dong':
            item['city'] = 39
        if city == 'Long An':
            item['city'] = 40
        if city == 'Nam Dinh':
            item['city'] = 41
        if city == 'Nghe An':
            item['city'] = 42
        if city == 'Ninh Binh':
            item['city'] = 43
        if city == 'Ninh Thuan':
            item['city'] = 44
        if city == 'Phu Tho':
            item['city'] = 45
        if city == 'Phu Yen':
            item['city'] = 46
        if city == 'Quang Binh':
            item['city'] = 47
        if city == 'Quang Nam':
            item['city'] = 48
        if city == 'Quang Ngai':
            item['city'] = 49
        if city == 'Quang Ninh':
            item['city'] = 50
        if city == 'Quang Trị':
            item['city'] = 51

        if city == 'Soc Trang':
            item['city'] = 52
        if city == 'Son La':
            item['city'] = 53
        if city == 'Tay Ninh':
            item['city'] = 54
        if city == 'Thai Bình':
            item['city'] = 55
        if city == 'Thai Nguyen':
            item['city'] = 56
        if city == 'Thanh Hoa':
            item['city'] = 57
        if city == 'hua Thien Hue':
            item['city'] = 58
        if city == 'Tien Giang':
            item['city'] = 59
        if city == 'Tra Vinh':
            item['city'] = 60
        if city == 'Tuyen Quang':
            item['city'] = 61
        if city == 'Vinh Long':
            item['city'] = 62
        if city == 'Vinh Phuc':
            item['city'] = 63
        if city == 'Yen Bai':
            item['city'] = 64
        if city == 'Toan quoc':
            item['city'] = 65
        if city == 'Nuoc ngoai':
            item['city'] = 66
        else:
            item['city'] = 1
        # 工作天数
        item['workday'] = ''
        # 工作开始时间
        item['work_time_start'] = ''
        # 工作结束时间
        item['work_time_end'] = ''
        # 职位描述
        desc = response.xpath('//*[@class="col-md-8  col-sm-12 tab-main-content"]/div[2]/div/text()').getall()
        sss = ''
        for i in desc:
            results = re.compile(r'[http|https]*://[a-zA-Z0-9.?/&=:]*', re.S)
            sss = sss + re.sub(results, '', i.strip()) + '<br>'
        item['desc'] = sss
        # 职业技能
        skills = response.xpath('//*[@class="col-md-8  col-sm-12 tab-main-content"]/div[3]/div/text()').getall()
        sss = ''
        for skill in skills:
            sss = sss + skill.strip() + '<br>'
        item['skills'] = sss
        # 工作福利
        job_benefits = response.xpath('//*[@class="benefit-name col-xs-11"]/text()').getall()
        sss = ''
        for i in job_benefits:
            sss = sss + i.strip() + '<br>'
        item['job_benefits'] = sss

        # 招聘数量
        item['hiring_count'] = ''
        # 联系人
        item['contact_name'] = response.xpath('//*[@class="box-summary"]/div[3]/div[2]/span[2]/text()').get()
        # 联系人电话
        item['contact_phone'] = ''
        # 联系人邮箱
        item['contact_email'] = ''
        # 招聘状态
        item['status'] = ''
        # 职能
        item['position'] = ''

        # # 浏览量
        item['view_cnt'] = ''
        # # 应用数量
        item['apply_cnt'] = ''
        # # 喜欢数量
        item['fev_cnt'] = ''
        # # 反馈数量
        item['fb_share_cnt'] = ''
        # # 共享数量
        item['zalo_share_cnt'] = ''
        # 标签
        item['tags'] = ''
        # 系统标签
        item['sys_tags'] = ''
        # 发布时间
        publish_time = response.xpath('//*[@class="box-summary link-list"]/div[1]/div[2]/span[2]/text()').get().strip()
        publish_time1 = datetime.datetime.strptime(publish_time, '%d/%m/%Y')

        # 传时间戳
        publish_times = time.strptime(publish_time, '%d/%m/%Y')
        item['publish_time'] = int(time.mktime(publish_times))
        # 过期时间
        expirce_time = response.xpath('//*[@class="expiry gray-light"]/text()').get().strip()
        expirce_time1 = int(re.findall('\d+', expirce_time)[0])
        expirce_time2 = publish_time1+datetime.timedelta(days=expirce_time1)
        a = expirce_time2.strftime('%d/%m/%y%y')
        expirce_time_day = time.strptime(a, '%d/%m/%Y')
        expire_time_1 = int(time.mktime(expirce_time_day))
        timeArray = time.localtime(expire_time_1)
        item['expire_time'] = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        # 定义空字典
        item1 = {}
        # 公司url
        item1['src_url'] = response.url

        item1['remark'] = ''
        # # 评论数量
        item1['cn_remark'] = ''
        # # 外部信息
        item1['ext_info'] = ''
        # # 公司描述
        company_desc = response.xpath('//*[@class="company-info"]/p/text()').getall()
        sss = ''
        for i in company_desc:
            results = re.compile(r'[http|https]*://[a-zA-Z0-9.?/&=:]*', re.S)
            sss= sss+re.sub(results, '', i)+'<br>'
        item1['company_desc'] = sss
        # 公司名
        item1['company_name'] = response.xpath('//*[@class="col-sm-12 company-name"]/a/text()').get().strip()
        # 公司营业执照
        item1['company_license'] = ''
        # 纳税人电话
        item1['tax_id_no'] = ''
        # 公司注册地址
        item1['register_add'] = ''
        # 办公地址
        item1['work_addr'] = response.xpath('//*[@class="box-summary"]/div[1]/div[2]/span[2]/text()').get()
        # 公司电话
        item1['mobile'] = ''
        # 公司官网
        item1['website'] = ''
        # 公司邮箱
        item1['email'] = ''
        # 招聘类型
        item1['entity_type'] = 0
        # 国家
        item1['country'] = 'VN'
        # 城市
        item1['city'] = item['city']
        # 行业
        item1['industry'] = item['industry']
        # 公司详情
        item['company_detail'] = json.dumps(item1, ensure_ascii=False)
        # 爬虫爬来的
        item['entry_type'] = 2
        yield item














