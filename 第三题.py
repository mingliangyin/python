# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:13:19 2018
第三题：
1.通过复制联网代码获得天气(老家)字典数据
2.打印温度temp,天气情况description,天气气压pre
@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/weather?q=chongqing&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
data['main']['temp']




import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/weather?q=fuling&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
print('温度为:'+str(data['main']['temp']),'气压为:'+str(data['main']['pressure']),'天气情况为:'+str(data['weather'][0]['description']))