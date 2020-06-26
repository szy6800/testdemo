# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExffItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    # 发布人
    creator = scrapy.Field()
    # 工作类型:1-全职,2-兼职,3-实习',
    work_type = scrapy.Field()
    # 薪资类型:1-月薪，2-周薪，3-日薪',
    salary_type = scrapy.Field()
    # 最小薪资
    min_salary = scrapy.Field()
    # 最大薪资
    max_salary = scrapy.Field()
    # 货币
    currency = scrapy.Field()
    # 行业
    industry = scrapy.Field()
    # 学历要求
    edu_level = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 工作天数
    workday = scrapy.Field()
    # 工作开始时间
    work_time_start = scrapy.Field()
    # 工作结束时间
    work_time_end = scrapy.Field()
    # 职位描述
    desc = scrapy.Field()
    # 职业技能
    skills = scrapy.Field()
    # 工作福利
    job_benefits = scrapy.Field()
    # 招聘数量
    hiring_count = scrapy.Field()
    # 联系人
    contact_name = scrapy.Field()
    # 联系人电话
    contact_phone = scrapy.Field()
    # 联系人邮箱
    contact_email = scrapy.Field()
    # 招聘状态
    status = scrapy.Field()
    # 工作经历
    expire_time = scrapy.Field()
    # 公司图片
    src_url = scrapy.Field()
    # 浏览量
    view_cnt = scrapy.Field()
    # 应用数量
    apply_cnt = scrapy.Field()
    # 喜欢数量
    fev_cnt = scrapy.Field()
    # 反馈数量
    fb_share_cnt = scrapy.Field()
    # 共享数量
    zalo_share_cnt = scrapy.Field()
    # 标签
    tags = scrapy.Field()
    # 系统标签
    sys_tags = scrapy.Field()
    # 评论
    remark = scrapy.Field()
    # 评论数量
    cn_remark = scrapy.Field()
    # 外部信息
    ext_info = scrapy.Field()
    # 发布时间
    publish_time = scrapy.Field()
    # 公司详细
    company_desc = scrapy.Field()
    # 公司名
    company_name = scrapy.Field()
    # 公司营业执照
    company_license = scrapy.Field()
    # 纳税人识别号
    tax_id_no = scrapy.Field()
    # 公司注册地址
    register_add = scrapy.Field()
    # 办公地址
    work_addr = scrapy.Field()
    # 公司电话
    mobile = scrapy.Field()
    # 公司官网
    website = scrapy.Field()
    # 公司邮箱
    email = scrapy.Field()
    # 分类
    entity_type = scrapy.Field()
    # 公司详情
    company_detail = scrapy.Field()
    # 爬虫
    entry_type = scrapy.Field()
    # 职能
    position = scrapy.Field()

