# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 09:22:13 2018
ctrl+1 注释代码
题目十六：高考派2300数据统计
1.根据2300下载的两百多M文件，统计招生总人数
2.统计7各地域的人数各是多少
3.计算比例
@author: Administrator
"""
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With': 'XMLHttpRequest'}
req=r.Request(url,headers=headers,data='id=477&type=2&city=23&state=1'.encode())
data=r.urlopen(req).read().decode('utf-8','ignore')

#东北
#黑龙江	吉林 	辽宁
area={'黑龙江':'东北','吉林':'东北','辽宁':'东北'}
areaplan={'东北':0}
areaplan['东北']=areaplan['东北']+8
###########通过下面定义多个变量赋值，计算出中国地区的人数
a=0
b=0
c=0
if '东北'==plan:
   a=a+1 

import json
data=json.loads(data)

for i in range(142600):
    if data['status']==1:
        ls=data['data']
    for school in ls:
        city=school['city']
        print(area[city])
        print(int(school['plan']))
        areaplan[area[city]]=areaplan[area[city]]+int(school['plan'])
        
#d='id=477&type=2&city=23&state=1'.encode()#bytes
#
#print(d)
#print(type(d))
        
        
        
        
f=open('./浙江文科招生1.txt','w')
import urllib.request as r
url='file:./all_school.txt'
data=r.urlopen(url).read().decode('utf-8')
import re
c=re.compile('http://www.gaokaopai.com/daxue-jianjie-(.*?).html',re.S).findall(data)
b=re.compile('(.*?)http:/').findall(data)
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
for i in range(len(c)):
   data='id={}&type=2&city=33&state=1'.format(c[i])
   data1=data.encode()
   req=r.Request(url,data=data1,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
   d=r.urlopen(req).read().decode('utf-8','ignore')
   print('输出次数{}'.format(i))
   f.write(d+"\n")
f.close()
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        