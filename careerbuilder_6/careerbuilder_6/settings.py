# -*- coding: utf-8 -*-

# Scrapy settings for careerbuilder_6 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'careerbuilder_6'

SPIDER_MODULES = ['careerbuilder_6.spiders']
NEWSPIDER_MODULE = 'careerbuilder_6.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'careerbuilder_6 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
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

'cookie': '__stdf=0; _gcl_au=1.1.1828053598.1590228451; _ga=GA1.2.1452378085.1590228451; _gid=GA1.2.531656898.1590228451; _fbp=fb.1.1590228454904.1643951873; __stat="BLOCK"; CBbyeIQBox=3-Sun May 24 2020; strSearchJobRecent=%7B%22_8%22%3A%22eyJMT0NBVElPTiI6IjgiLCJzaW1pbGFyIjowLCJPV05FUiI6ImtpZW12aWVjIiwiQ09VTlRfU0VBUkNIIjp0cnVlfQ%3D%3D%22%7D; jsk_first_name_client=shi; jsk_last_name_client=zhangyi; jsk_email_client=1198558613%40qq.com; __stp={"visit":"returning","uuid":"60a6d4f0-fe11-42be-ae27-c83a8e7f67ae","ck":"1198558613@qq.com"}; stickyBox=0; __zi=2000.SSZzejyD6zyvZ_knpnqNmJ-VuFFT5aV3Qu6k_SLK6z5Xdxo_rq88tZ-KkVIQH0pSEPgx-D5C2zrrchhuqqiArJ4r.1; _hjid=f2375e27-7a3b-4885-b8f2-1e3cbc468744; __stbpnenable=1; intNumberWrongPass=0-20200528; clientKey=1198558613%40qq.com; unique_client=94be4c5b0711393e472de55a4198bbf1; _hjAbsoluteSessionInProgress=1; fpsend=147282; __tawkuuid=e::careerbuilder.vn::QJt308cenRqj3g5/4ni42WNQ52SKy76wRYU7a8vbznGYFq3DKbXBGiCwvWg2s0bT::2; employeers=99ljtkapc89vjpue2ka6fejdj3; TawkConnectionTime=0; jobseeker=1k2feftq5vs4gcmjb8t27dbc04; __sts={"sid":1590651856523,"tx":1590652525866,"url":"https%3A%2F%2Fcareerbuilder.vn%2Fvi%2Ftim-viec-lam%2Fsales-engineer-automation-id-494901.35B40E9D.html","pet":1590652525866,"set":1590651856523,"pUrl":"https%3A%2F%2Fcareerbuilder.vn%2Fviec-lam%2Ftat-ca-viec-lam-vi.html","pPet":1590652516130,"pTx":1590652516130}; __stgeo="granted"'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'careerbuilder_6.middlewares.Careerbuilder6SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'careerbuilder_6.middlewares.UserAgentDownloadMiddleware': 543,
   'careerbuilder_6.middlewares.IPProxyDownloadMiddleware': 541,


}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'careerbuilder_6.pipelines.Careerbuilder6Pipeline': 300,
}

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
