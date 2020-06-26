# -*- coding: utf-8 -*-
import json
import re
import time
from copy import deepcopy

import scrapy

from careerlink.items import CareerlinkItem



class CareerSpider(scrapy.Spider):
    name = 'career'
    allowed_domains = ['careerlink.vn']
    start_urls = ['https://www.careerlink.vn/vieclam/list?page={}'.format(i) for i in range(1,5)]

    def parse(self, response):
        item = CareerlinkItem()

        job_list_url = response.xpath('//h2[@class="list-group-item-heading"]/a/@href').getall()

        for href in job_list_url:
            item['src_url'] = response.urljoin(href)

            yield scrapy.Request(item['src_url'], callback=self.parse_info, meta={'item': deepcopy(item)}, dont_filter=True)

    def parse_info(self, response):
        # 传参数
        item = response.meta['item']
        # 职位名称
        item['name'] = response.xpath('//*[@itemprop="title"]/text()').get().strip()
        # 发布人
        item['creator'] = ''
        # 工作类型1-全职,2-兼职,3-实习',
        item['work_type'] = 1
        # 工资类型1-月薪，2-周薪，3-日薪',
        item['salary_type'] = 1
        # 最小薪资
        try:
            item['min_salary'] = int(response.xpath('//*[@itemprop="minValue"]/@content').get())

            # 最大薪资
            item['max_salary'] = int(response.xpath('//*[@itemprop="maxValue"]/@content').get())
        except:
            pass
        # 货币
        item['currency'] = 'VND'
        # # 行业
        industry = response.xpath('//*[@class="list-unstyled"]//ul[1]/li/a/span/text()').getall()
        sss = ''
        for i in industry:
            sss = sss+i.strip()+'||'
        item['industry'] = sss

        # 学历要求
        try:
            edu_level = response.xpath('//*[@class="list-unstyled"]/li[4]/span/text()').get().strip()
            # 不限学历
            if edu_level == 'Không yêu cầu':
                item['edu_level'] = 0
            # 高中
            elif edu_level == 'Trung cấp':
                item['edu_level'] = 1
            elif edu_level == 'Trung cấp trở lên':
                item['edu_level'] = 1
            # 大学专科
            elif edu_level == 'Đại học':
                item['edu_level'] = 2
            elif edu_level == 'Đại học trở lên':
                item['edu_level'] = 2
            # 大学本科
            elif edu_level == 'Cao đẳng':
                item['edu_level'] = 2
            elif edu_level == 'Cao đẳng trở lên':
                item['edu_level'] = 2
            #研究生
            elif edu_level == 'bác sĩ':
                item['edu_level'] = 3
            elif edu_level == 'bác sĩ trở lên':
                item['edu_level'] = 3
            #博士
            elif edu_level == 'tiến sĩ':
                item['edu_level'] = 4
            elif edu_level == 'tiến sĩ trở lên':
                item['edu_level'] = 4
            else:
                item['edu_level'] = 0
        except:
            pass
        # 国家
        item['country'] = 'VN'
        # 城市
        city = response.xpath('//*[@itemprop="addressRegion"]/text()').get()
        if city == 'Hồ Chí Minh':
            item['city'] = 1
        elif city == 'Hà Nội':
            item['city'] = 2
        elif city == 'An Giang':
            item['city'] = 3
        elif city == 'Bạc Liêu':
            item['city'] = 4
        elif city == 'Bà Rịa-Vũng Tàu':
            item['city'] = 5
        elif city == 'Bắc Cạn':
            item['city'] = 6
        elif city == 'Bắc Giang':
            item['city'] = 7
        elif city == 'Bắc Ninh':
            item['city'] = 8
        elif city == 'Bến Tre':
            item['city'] = 9
        elif city == 'Bình Dương':
            item['city'] = 10
        elif city == 'Bình Định':
            item['city'] = 11
        elif city == 'Bình Phước':
            item['city'] = 12
        elif city == 'Bình Thuận':
            item['city'] = 13
        elif city == 'Cao Bằng':
            item['city'] = 14
        elif city == 'Cà Mau':
            item['city'] = 15
        elif city == 'Cần Thơ':
            item['city'] = 16
        elif city == 'Đà Nẵng':
            item['city'] = 17
        elif city == 'Đắk Lắk':
            item['city'] = 18
        elif city == 'Đắk Nông':
            item['city'] = 19
        elif city == 'Điện Biên':
            item['city'] = 20
        elif city == 'Đồng Nai':
            item['city'] = 21
        elif city == 'Đồng Tháp':
            item['city'] = 22
        elif city == 'Gia Lai':
            item['city'] = 23
        elif city == 'Hà Giang':
            item['city'] = 24
        elif city == 'Hà Nam':
            item['city'] = 25
        elif city == 'Hà Tĩnh':
            item['city'] = 27
        elif city == 'Hải Dương':
            item['city'] = 28
        elif city == 'Hải Phòng':
            item['city'] = 29
        elif city == 'Hậu Giang':
            item['city'] = 30
        elif city == 'Hòa Bình':
            item['city'] = 31
        elif city == 'Hưng Yên':
            item['city'] = 32
        elif city == 'Khánh Hòa':
            item['city'] = 33
        elif city == 'Kiên Giang':
            item['city'] = 34
        elif city == 'Kon Tum':
            item['city'] = 35
        elif city == 'Lai Châu':
            item['city'] = 36
        elif city == 'Lạng Sơn':
            item['city'] = 37
        elif city == 'Lào Cai':
            item['city'] = 38
        elif city == 'Lâm Đồng':
            item['city'] = 39
        elif city == 'Long An':
            item['city'] = 40
        elif city == 'Nam Định':
            item['city'] = 41
        elif city == 'Nghệ An':
            item['city'] = 42
        elif city == 'Ninh Bình':
            item['city'] = 43
        elif city == 'Ninh Thuận':
            item['city'] = 44
        elif city == 'Phú Thọ':
            item['city'] = 45
        elif city == 'Phú Yên':
            item['city'] = 46
        elif city == 'Quảng Bình':
            item['city'] = 47
        elif city == 'Quảng Nam':
            item['city'] = 48
        elif city == 'Quảng Ngãi':
            item['city'] = 49
        elif city == 'Quảng Ninh':
            item['city'] = 50
        elif city == 'Quảng Trị':
            item['city'] = 51
        elif city == 'Sóc Trăng':
            item['city'] = 52
        elif city == 'Sơn La':
            item['city'] = 53
        elif city == 'Tây Ninh':
            item['city'] = 54
        elif city == 'Thái Bình':
            item['city'] = 55
        elif city == 'Thái Nguyên':
            item['city'] = 56
        elif city == 'Thanh Hóa':
            item['city'] = 57
        elif city == 'hừa Thiên Huế':
            item['city'] = 58
        elif city == 'Tiền Giang':
            item['city'] = 59
        elif city == 'Trà Vinh':
            item['city'] = 60
        elif city == 'Tuyên Quang':
            item['city'] = 61
        elif city == 'Vĩnh Long':
            item['city'] = 62
        elif city == 'Vĩnh Phúc':
            item['city'] = 63
        elif city == 'Yên Bái':
            item['city'] = 64
        elif city == 'Toàn quốc':
            item['city'] = 65
        elif city == 'Nước ngoài':
            item['city'] = 66
        else:
            item['city'] = 1
        # 工作天数
        item['workday'] = ''
        # 工作开始时间
        item['work_time_start'] = ''
        # 工作结束时间
        item['work_time_end'] = ''
        #职能
        item['position'] = ''
        # 职位描述
        desc = response.xpath('//*[@itemprop="description"]/p/text()').getall()
        sss = ''
        for i in desc:
        # 去除超链接
            results = re.compile(r'[http|https]*://[a-zA-Z0-9.?/&=:]*', re.S)
            sss = sss +re.sub(results, '', i)+'<br>'
        item['desc'] = sss

        # 职业技能
        skills = response.xpath('//*[@itemprop="skills"]/p/text()').getall()
        sss = ''
        for i in skills:
            results = re.compile(r'[http|https]*://[a-zA-Z0-9.?/&=:]*', re.S)
            sss = sss + re.sub(results, '', i)+'<br>'
        item['skills'] = sss
        # 工作福利
        item['job_benefits'] = ''
        # 招聘数量
        item['hiring_count'] = ''
        # 联系人
        contact_name = response.xpath('//div[@class="job-side-data"]/ul/li[2]/text()').get().strip()
        item['contact_name'] = contact_name.split(':')[1].strip()
        #联系电话
        # a = response.body
        # re.findall('<span itemprop="telephone">(.*?)</span>',a)
        # re.findall('Tên liên hệ:(.*?)',a,re.S)
        try:
            item['contact_phone'] = re.findall('<span itemprop="telephone">(.*?)</span>',response.text)[0]
        # 联系人邮箱
            item['contact_email'] = re.findall('<span itemprop="email">(.*?)</span>',response.text)[0]
        except:
            pass
        # 招聘状态
        item['status'] = ''
        # 过期时间
        expire_time = response.xpath('//*[@class="job-data"]/dl/dd[2]/text()').get().strip()
        expire_time_day = time.strptime(expire_time, '%d/%m/%Y')
        expire_time1 = int(time.mktime(expire_time_day))
        timeArray = time.localtime(expire_time1)
        item['expire_time'] = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

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
        publish_time = response.xpath('//*[@class="job-data"]/dl/dd[1]/text()').get().strip()
        # #传时间戳
        publish_times = time.strptime(publish_time, '%d/%m/%Y')
        item['publish_time'] = int(time.mktime(publish_times))

        # 定义
        item1 = {}
        item1['remark'] = ''
        # # 评论数量
        item1['cn_remark'] = ''
        # # 外部信息
        item1['ext_info'] = ''
        # # 公司描述
        company_desc = response.xpath('//div[@class="job-side-data"]/div/p//text()').getall()
        sss = ''
        for i in company_desc:
            results = re.compile(r'[http|https]*://[a-zA-Z0-9.?/&=:]*', re.S)
            sss = sss+re.sub(results, '', i)+'<br>'
        item1['company_desc'] = sss
        # 公司名
        item1['company_name'] = response.xpath('//*[@itemprop="name"]/text()').get().strip()
        # 公司营业执照
        item1['company_license'] = ''
        # 纳税人电话
        item1['tax_id_no'] = ''
        # 公司注册地址
        item1['register_add'] = ''
        item['entry_type'] = 2
        # 办公地址
        work_addr1 = response.xpath('//*[@itemprop="address"]/span[1]/text()').get().strip()
        work_addr2 = response.xpath('//*[@itemprop="address"]/span[2]/text()').get().strip()
        item1['work_addr'] = work_addr1+work_addr2
        # 公司电话
        item1['mobile'] = ''
        # 公司官网
        website = response.xpath('//*[@itemprop="url"]/a/@href').get()
        if website =='':
            item1['website'] ='https://www.careerlink.vn'
        else:
            item1['website'] = website
        # 公司邮箱
        item1['email'] = ''
        # 公司详情页
        item1['src_url'] = response.url
        # 招聘类型
        item1['entity_type'] = 0
        #国家
        item1['country'] = 'VN'
        #城市
        item1['city'] = item['city']
        # 行业
        item1['industry'] = item['industry']

        item['company_detail'] = json.dumps(item1,ensure_ascii=False)

        yield item


