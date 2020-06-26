import json
import re
import pprint
import requests


url = 'https://h5api.m.taobao.com/h5/mtop.alimama.union.sem.landing.pc.items/1.0/?jsv=2.4.0&appKey=12574478&t=1593182466111&sign=deb78dd4e83d042872c7df3ecd043a54&api=mtop.alimama.union.sem.landing.pc.items&v=1.0&AntiCreep=true&dataType=jsonp&type=jsonp&ecode=0&callback=mtopjsonp1&data=%7B%22keyword%22%3A%22%E5%A5%B3%E8%A3%85%22%2C%22ppath%22%3A%22%22%2C%22loc%22%3A%22%22%2C%22minPrice%22%3A%22%22%2C%22maxPrice%22%3A%22%22%2C%22ismall%22%3A%22%22%2C%22ship%22%3A%22%22%2C%22itemAssurance%22%3A%22%22%2C%22exchange7%22%3A%22%22%2C%22custAssurance%22%3A%22%22%2C%22b%22%3A%22%22%2C%22clk1%22%3A%22633a46e6f88ea5ddee58345b2ae5ed2c%22%2C%22pvoff%22%3A%22%22%2C%22pageSize%22%3A%22100%22%2C%22page%22%3A%222%22%2C%22elemtid%22%3A%221%22%2C%22refpid%22%3A%22mm_26632258_3504122_32538762%22%2C%22pid%22%3A%22430673_1006%22%2C%22featureNames%22%3A%22spGoldMedal%2CdsrDescribe%2CdsrDescribeGap%2CdsrService%2CdsrServiceGap%2CdsrDeliver%2C%20dsrDeliverGap%22%2C%22ac%22%3A%22rV8oFrRusxACAXO3BY5sqHfe%22%2C%22wangwangid%22%3A%22%22%2C%22catId%22%3A%22%22%7D'

headers = {
  'referer': 'https://uland.taobao.com/sem/tbsearch?spm=a2e15.8261149.07626516003.1.694a29b4nI8ATF&refpid=mm_26632258_3504122_32538762&keyword=%E5%A5%B3%E8%A3%85&clk1=633a46e6f88ea5ddee58345b2ae5ed2c&upsid=633a46e6f88ea5ddee58345b2ae5ed2c&page=2&_input_charset=utf-8',
'cookie': 'thw=cn; sgcookie=EIIBbzosWG6Ahafnbr%2FBD; tracknick=; cna=rV8oFrRusxACAXO3BY5sqHfe; hng=CN%7Czh-CN%7CCNY%7C156; miid=182359712542986543; t=7345620ff9583576130bd812ea588b5e; tfstk=crxNBb6f_cnNLrjjyGsVhpTQ17JOawfcNkWPSUg4qAQ3nYbVas2aM9DQM9WVwDbG.; _m_h5_tk=b2b3582b234488675c904342d111d1d2_1593190655923; _m_h5_tk_enc=1e1fba54bcde0e43401b5c02b56e1854; isg=BPHxreBdC3Z2A6Q1MhLs4AubAH2L3mVQ8KJB7tMFlrlR-hVMGyw1II1bHI6cMv2I; l=eBQF_-Vmq2ckxCR_BO5Z-urza77TWQOfGsPzaNbMiIncC6pG9o9O2J-QLGCJWdKRR8XcGyTB4sz4jMwt-FT8JikBhzbSZRpVBvn6pef..',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'

}
a = requests.get(url,headers=headers).text
pprint.pprint(a)
#
# b = re.findall('"data":{.*}',a)[0]
# print(b)
