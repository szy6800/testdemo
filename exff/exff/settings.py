# -*- coding: utf-8 -*-

# Scrapy settings for exff project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'exff'

SPIDER_MODULES = ['exff.spiders']
NEWSPIDER_MODULE = 'exff.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'exff (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:

DEFAULT_REQUEST_HEADERS = {

  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
'Cookie':'_gcl_au=1.1.88279036.1590039250; _ga=GA1.1.1631438367.1590039250; suggest_course_ab_testing_reset=6; suggest_course_ab_testing=B; user_on_board_ab_testing_reset=3; user_on_board_ab_testing=A; _fbp=fb.1.1590041981423.2031077612; __utmz=136564663.1590115505.9.8.utmcsr=vnw_header_menu|utmccn=(not%20set)|utmcmd=TopManagementJobs|utmctr=homepage2; VNWSearchJob[keyword]=; fs_uid=rs.fullstory.com#NYSW7#6338902534275072:6294928192847872/1621850687; __utmc=136564663; _hjid=0516def8-ea25-48f9-b711-cedb876f8c2b; _hjMinimizedPolls=501507; _hjDonePolls=501507; recommend_jobs_logout_ab_testing_reset=1; recommend_jobs_logout_ab_testing=B; my_job_alert_ab_testing_reset=2; my_job_alert_ab_testing=B; __utmv=136564663.|1=Job%20Detail%20Display=VB=1^5=My%20Job%20Alert%20Display=VB=1; VNWSearchJob[city]=all; lang=2; PHPSESSID=bhqg6kge64aumfc9a7sdb85gr7; VNW128450527232960=mpyhomvWnZhdj3%2BIb6CenmmtysVYvH66baKfz2%2BnoJtci3qNaZ2c; VNWJSAll128450527232960=mpyhomvWnZhdj3%2BIb6CenmmtysVYvH66baKfz2%2BnoJtci3qNaZ2c%7Cbhqg6kge64aumfc9a7sdb85gr7; VNWWS128450527232960=iL3W14bJz5dznYnBk7275ZHJqZdz05zQh62z54Xvtsp1nZzPktPNn4XJwspzra6Lkta414bftsp1rZyJh623ooe5tZV0w5CLk73NoYbJqdpzoJ3BhtDmvGq637x9onikkMLiyI%2B6mrCgxbKvs7rjvX%2FCmbBqvbSja7PXvKLg37yQnnikjczkyIy%2Bnbx6q7GvkL%2FVu3zGmK99r7Sjfaqfu6W70rFqm7Gko7KbvYk%3D; VNW_WS_COOKIE=iL3W14bJz5dznYnBk7275ZHJqZdz05zQh62z54Xvtsp1nZzPktPNn4XJwspzra6Lkta414bftsp1rZyJh623ooe5tZV0w5CLk73NoYbJqdpzoJ3BhtDmvGq637x9onikkMLiyI%2B6mrCgxbKvs7rjvX%2FCmbBqvbSja7PXvKLg37yQnnikjczkyIy%2Bnbx6q7GvkL%2FVu3zGmK99r7Sjfaqfu6W70rFqm7Gko7KbvYk%3D; VNW_USER_COOKIE=mpyhomvWnZhdj3%2BIb6CenmmtysVYvH66baKfz2%2BnoJtci3qNaZ2c; __utma=136564663.751161361.1590039250.1590467186.1590481029.24; FIREBASE_JWT=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJ2aWV0bmFtd29ya3MtbWVzc2FnZUB2aWV0bmFtd29ya3MtbWVzc2FnZS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsInN1YiI6InZpZXRuYW13b3Jrcy1tZXNzYWdlQHZpZXRuYW13b3Jrcy1tZXNzYWdlLmlhbS5nc2VydmljZWFjY291bnQuY29tIiwiYXVkIjoiaHR0cHM6XC9cL2lkZW50aXR5dG9vbGtpdC5nb29nbGVhcGlzLmNvbVwvZ29vZ2xlLmlkZW50aXR5LmlkZW50aXR5dG9vbGtpdC52MS5JZGVudGl0eVRvb2xraXQiLCJpYXQiOjE1OTA0ODEwMzcsImV4cCI6MTU5MDQ4NDYzNywidWlkIjo2MjM3MDQyfQ.OECkC01FqlVJxQmqozkpdvyPnyWElZ7M8nMCkwpRQ6K9n8Rm-eab51GHKmsl6lLPMWtw8UOEaoLTtoJdAciU96-Ojg3jiLgtVJeGK5NDJpWk0k7KaRSN0hnT_tQJbByIZpCGeWXl432cmymt3uUdhQ37XmPWlBxhyXkQPyDPi-Bb0HNsbMiL3tSRZdpjZxDghYO7ARRq_VD7Y_aVEXBcLyc7B2SX5CYk5VgFzJFWJfzrmBSrIqZxcloqcTzs6_kJyWpNlHmushxGUezrVdFAj-vBek8xi9b3VVJuTS2ylgiUriw4u-ojsCF5dnjaTY0HFO-5kiQvWReCSNzuxmNViQ; VNW_LAST_JOB_SEEN=1249926%2C6237042; __utmt=1; __utmb=136564663.3.10.1590481029; _ga_0GGBQ5L5MF=GS1.1.1590481029.24.1.1590482074.0; next-i18next=vi',

}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'exff.middlewares.ExffSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'exff.middlewares.IPProxyDownloadMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'exff.pipelines.ExffPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
