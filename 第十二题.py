# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:48:22 2018
全球未来5天气预报
2018-06-21 03:00:00    按照3小时一次预报
2018-06-21 06:00:00
2018-06-21 09:00:00------当前时间
2018-06-21 12:00:00
2018-06-25 21:00:00

题目十二：使用re爬取天气信息
1.天气描述，天气温度，天气气压



@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=hamburg,de&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import re
ls1=re.compile('"dt_txt":"(.*?)"').findall(data)
ls2=re.compile('"description":"(.*?)"').findall(data)
ls3=re.compile('"temp":(.*?),').findall(data)
ls4=re.compile('"pressure":(.*?),').findall(data)
for i in range(0,37):
    print('时间：{},天气：{},温度：{},气压：{}'.format(ls1[i],ls2[i],ls3[i],ls4[i]))















#讲str类型转换为dict

import json
data=json.loads(data)
#data字典-》list列表-》index 0 字典-》main字典-》temp变量
data['list'][0]['main']['temp']
#data字典-》list列表-》index 0 字典-》main字典-》temp_max变量

#data字典-》list列表-》index 0 字典-》main字典-》temp_min变量
