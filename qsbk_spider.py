# -*- coding:utf-8 -*-
import urllib
import urllib.request
import urllib.error
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

try:
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    a = '<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class' + '="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>'

    #a = '<h2>.+?</h2>'

    print(a)

    pattern = re.compile(a, re.S)

    items = re.findall(pattern, content)
    for item in items:
        #print(item[0])
        #haveImg = re.search("img",item[3])
        #if not haveImg:
        print(item[0])

    #print(response.read())
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)