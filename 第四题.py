# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:48:22 2018
全球未来5天气预报
2018-06-21 03:00:00    按照3小时一次预报
2018-06-21 06:00:00
2018-06-21 09:00:00------当前时间
2018-06-21 12:00:00
2018-06-25 21:00:00

第四题：求出未来5天天气
1.打印每天的6:00,12:00,18:00的天气(城市,温度，情况，气压，最高温度，最低温度)
2.同上写出[英文版的]
3.根据天气的情况，给出建议：例如，今天下雨，提示带伞。今天温度高，穿衬衫...三个件以上
4.根据温度打印出问题折线图
    28——————————————————————————————
    30——————————————————————————————————
    10——————————————————
5.打印出其他10个城市的天气，计算出天气排名，按着大到小的顺序。



@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》list列表-》index 0 字典-》main字典-》temp变量
data['list'][0]['main']['temp']
#data字典-》list列表-》index 0 字典-》main字典-》temp_max变量

#data字典-》list列表-》index 0 字典-》main字典-》temp_min变量
