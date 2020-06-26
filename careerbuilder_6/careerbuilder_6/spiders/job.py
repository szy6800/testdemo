# -*- coding: utf-8 -*-
import datetime
import math
import time

import scrapy

from careerbuilder_6.items import Careerbuilder6Item
import json
import pprint
import re
from copy import deepcopy
class JobSpider(scrapy.Spider):
    name = 'job'

    allowed_domains = ['careerbuilder.vn']
    #所有网站信息来源

    start_urls = ['https://careerbuilder.vn/viec-lam/tat-ca-viec-lam-trang-{}-vi.html'.format(i) for  i in range(10,15)]

    def parse(self, response):
        #列表页url
        item = Careerbuilder6Item()
        hrefs = response.xpath('//*[@class="job_link"]/@href').getall()
        # 发布时间
        publish_times = response.xpath('//*[@class="time"]/time/text()').getall()

        for href,publish_time in zip(hrefs,publish_times):
            item['src_url']=response.urljoin(href)
            publish_time_day = time.strptime(publish_time, '%d/%m/%Y')
            #发布时间

            item['publish_time'] = int(time.mktime(publish_time_day))
            try:
                yield scrapy.Request(item['src_url'], callback=self.parse_info, meta={'item': deepcopy(item)},dont_filter=True)
            except:
                pass

    def parse_info(self, response):
        item = response.meta['item']
        #职位名称
        item['name'] = response.xpath('//*[@class="title"]/text()').get()
        #发布人
        item['creator'] = ''
        # 工作类型
        item['work_type'] = 1
        #工资类型
        item['salary_type'] = 2
        try:
            # 最小薪资
            min_salary_str = response.xpath("//*[@class='salary']/p/text()").get()
            min_salary = min_salary_str.split('$')[1]
            min_salary = re.sub('\s','',min_salary)
            if min_salary == 'Cạnhtranh':
                item['min_salary']=0
            if 'USD' in min_salary_str:
                a = min_salary_str.replace(',','')
                min_salary = int(re.findall('\d+', a)[0])
                min_salary1 = int(min_salary*23200)
                min_salary2 = min_salary1/1000000
                item['min_salary'] = math.floor(min_salary2)*1000000
            else:
                min_salary = response.xpath("//*[@class='salary']/p/text()").get()
                min_salary1 = int(re.findall('\d+', min_salary)[0])
                min_salary1 = min_salary1 * 1000000
                min_salary2 = int(min_salary1) / 1000000
                item['min_salary'] = math.floor(min_salary2)*1000000
            # 最大薪资
            max_salary_str = response.xpath("//*[@class='salary']/p/text()").get()
            max_salary = max_salary_str.split('$')[1]
            max_salary = str(re.sub('\s', '', max_salary))
            if max_salary == 'Cạnhtranh':
                item['max_salary'] = 0
            if 'USD' in max_salary_str:
                a = max_salary_str.replace(',', '')
                max_salary = int(re.findall('\d+', a)[1])
                max_salary1 = int(max_salary * 23200)
                max_salary2 = max_salary1 / 1000000
                item['max_salary'] = math.ceil(max_salary2) * 1000000
            else:
                max_salary = response.xpath("//*[@class='salary']/p/text()").get()
                max_salary1 = int(re.findall('\d+', max_salary)[1])
                max_salary1 = max_salary1*1000000
                max_salary2 = int(max_salary1)/1000000
                item['max_salary'] = math.ceil(max_salary2) * 1000000
        except:
            pass
        # 货币
        item['currency'] = 'VND'
        # 行业
        industry= response.xpath('//*[@class="industry"]/p/a/text()').getall()
        sss = ''
        for i in industry:
            sss = sss + i.strip() + "||"
            sss = re.sub('\r\n','',sss)
            a = re.sub('                                        ','',sss)
            sss = a.replace(',','')
        item['industry'] = sss

        #学历要求
        try:
            edu_level = response.xpath('//*[@class="content_fck"]/ul/li[1]/text()').get().strip()
            edu_level = re.split(':',edu_level)[1].replace('\r\n','').strip()
            # 不限
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
                # 研究生
            elif edu_level == 'bác sĩ':
                item['edu_level'] = 3
            elif edu_level == 'bác sĩ trở lên':
                item['edu_level'] = 3
                # 博士
            elif edu_level == 'tiến sĩ':
                item['edu_level'] = 4
            elif edu_level == 'tiến sĩ trở lên':
                item['edu_level'] = 4
            else:
                item['edu_level'] = 0
        except:
            pass
        #国家
        item['country'] = 'VN'
        #城市
        city = response.xpath('//*[@class="map"]/p/a/text()').get()
        if city =='Hồ Chí Minh':
            item['city'] = 1
        elif city =='Hà Nội':
            item['city'] = 2
        elif city =='An Giang':
            item['city'] = 3
        elif city =='Bạc Liêu':
            item['city'] = 4
        elif city =='Bà Rịa-Vũng Tàu':
            item['city'] = 5
        elif city =='Bắc Cạn':
            item['city'] = 6
        elif city =='Bắc Giang':
            item['city'] = 7
        elif city =='Bắc Ninh':
            item['city'] = 8
        elif city =='Bến Tre':
            item['city'] = 9
        elif city == 'Bình Dương':
            item['city'] = 10
        elif city == 'Bình Định':
            item['city'] = 11
        elif city =='Bình Phước':
            item['city'] = 12
        elif city =='Bình Thuận':
            item['city'] = 13
        elif city =='Cao Bằng':
            item['city'] = 14
        elif city =='Cà Mau':
            item['city'] = 15
        elif city =='Cần Thơ':
            item['city'] = 16
        elif city =='Đà Nẵng':
            item['city'] = 17
        elif city =='Đắk Lắk':
            item['city'] = 18
        elif city =='Đắk Nông':
            item['city'] = 19
        elif city =='Điện Biên':
            item['city'] = 20
        elif city =='Đồng Nai':
            item['city'] = 21
        elif city =='Đồng Tháp':
            item['city'] = 22
        elif city =='Gia Lai':
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

        #工作天数
        item['workday'] = ''
        # 工作开始时间
        item['work_time_start'] = ''
        # 工作结束时间
        item['work_time_end'] = ''
        # 职位描述
        desc = response.xpath('//*[@class="job-detail-content"]/div[3]//text()').getall()
        sss = ''
        for i in desc:
            b = sss+i.strip()+'<br>'
            sss = b.replace('<br>Mô tả Công việc<br><br>', '')

        item['desc'] = sss
        # 职业技能
        skills = response.xpath('//*[@class="job-detail-content"]/div[4]//text()').getall()
        sss = ''
        for i in skills:
            a  = sss + i.strip() + '<br>'
            sss = a.replace('<br>Yêu Cầu Công Việc<br><br>', '')
        item['skills'] = sss
        # 工作福利
        job_benefits =response.xpath('//*[@class="welfare-list"]/li/text()').getall()
        sss = ''
        for i in job_benefits:
            sss = sss + i + '<br>'
        item['job_benefits'] = sss
        # 招聘数量
        item['hiring_count'] = ''
        # 联系人
        item['contact_name'] = ''
        # 联系人电话
        item['contact_phone'] = ''
        # 联系人邮箱
        item['contact_email'] = ''

        item['position'] = ''
        # 招聘状态
        item['status'] = ''
        # 过期时间
        try:
            expire_timea = response.xpath('//*[@class="detail-box has-background"]/ul/li[3]/p/text()').get()
            if expire_timea is not None:
                expirce_time_day = time.strptime(expire_timea, '%d/%m/%Y')
                expire_time_1 = int(time.mktime(expirce_time_day))
                timeArray = time.localtime(expire_time_1)
                item['expire_time'] = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            else:
                expire_timea = response.xpath('//*[@class="detail-box has-background"]/ul/li[2]/p/text()').get()
                expirce_time_day = time.strptime(expire_timea, '%d/%m/%Y')
                expire_time_1 = int(time.mktime(expirce_time_day))
                timeArray = time.localtime(expire_time_1)
                item['expire_time'] = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        except:
            pass


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
        # # 标签
        item['tags'] = ''
        # # 系统标签
        item['sys_tags'] = ''
        item['entry_type'] = 2
        src_url = response.xpath('//*[@id="tabs-job-company"]/a/@href').get()
        try:

            yield scrapy.Request(src_url,callback=self.company_info, meta={'item': deepcopy(item)},dont_filter=True)
        except:
            pass

    def company_info(self,response):
        item = response.meta['item']
        item1 = {}
        # # 评论
        item1['remark'] = ''
        # # 评论数量
        item1['cn_remark'] = ''
        # # 外部信息
        item1['ext_info'] = ''
        # # 公司描述
        company_desc = response.xpath('//*[@class="col-lg-12"]/div//text()').getall()
        sss = ''
        for i in company_desc:
            sss = sss+i+'<br/>'
        item1['company_desc'] = sss
        # 公司名
        item1['company_name'] = response.xpath('//*[@class="content"]/p/text()').get()
        # 公司营业执照
        item1['company_license'] = ''
        # 纳税人电话
        item1['tax_id_no'] = ''
        # 公司注册地址
        item1['register_add'] = ''
        # 办公地址
        item1['work_addr'] = response.xpath('//*[@class="content"]/p[2]/text()').get()
        # 公司电话
        item1['mobile'] = ''
        # 公司官网
        item1['website'] = ''
        # 公司邮箱
        item1['email'] = ''
        # 招聘类型
        item1['entity_type'] = 0
        #公司url
        item1['src_url'] = response.url
        # 国家
        item1['country'] = 'VN'
        # 城市
        item1['city'] = item['city']
        # 行业
        item1['industry'] = item['industry']
        # 公司详情
        item['company_detail'] = json.dumps(item1, ensure_ascii=False)

        yield item




















