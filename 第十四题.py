 -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:14:07 2018
题目十四：家长帮大数据爬虫项目
1.根据all_school.txt获取全中国学校网址编号：1304，生成一个2300列表
2.根据http://www.gaokaopai.com/daxue-zhaosheng-学校编号.html 获取全国城市的编号 例如北京：11
3.班级团队(需要下载142600(2300*31*2)次)：
    中国划分区域-分组(城市)
    区域分组员
    如何下载策略-分时间下载
    执行人物2300-分配到自己的任务一般是2300
    保存数据---组长全部合并--班长统计
4.待定

@author: Administrator
"""

f=open('./all_school.txt',encoding='UTF-8')
ls=f.readlines()#将所有的文本中的每行读取到一个列表中去
ls=str(ls)
import re
ls=re.compile('jianjie-(.*?).html').findall(ls)
print(ls)



######################################################




import re
url='http://www.gaokaopai.com/daxue-0-0-0-0-0-0-0.html'
data='id=2948&type=2&city=50&state=1'.encode()
req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
d=r.urlopen(req).read().decode('utf-8','ignore')
e=re.compile('<span><a href="http://www.gaokaopai.com/daxue-(.*?)-0-0-0-0-0-0.html">').findall(d) 
f=re.compile('<span><a href="http://www.gaokaopai.com/daxue-..-0-0-0-0-0-0.html">(.*?)</a></span>').findall(d)
for i in range(len(e)):
    print('{}-{}'.format(f[i],e[i]))
    
###################################################
    

import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
for i in ls:    
    data='id={}&type=1&city=32&state=1'.format(i).encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    d=r.urlopen(req).read().decode('utf-8','ignore')
    e=re.compile('"plan":\S(.*?)\S,').findall(d)
    print(e)
f=open('./d.txt','w')
f.write(d+"\n")
f.close()
    
############################################################  
import json
f=open('./cd.txt','w',encoding='utf-8')
for i in ls:
    try:
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=1&city=32&state=1'.format(i).encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        d=r.urlopen(req).read().decode('utf-8','ignore')
        ls1=json.loads(d)
        for i in range(len(ls1['data'])):
            ls2=ls1['data'][i]['school']
            ls3=ls1['data'][i]['city']
            ls4=ls1['data'][i]['profess']
            ls5=ls1['data'][i]['subject']
            ls6=ls1['data'][i]['plan']
            print('学校：{},城市：{},专业：{},科类：{},录取人数：{}'.format(ls2,ls3,ls4,ls5,ls6))
            f.write('学校：{},城市：{},专业：{},科类：{},录取人数：{}'.format(ls2,ls3,ls4,ls5,ls6))
        f.write('\n')
except Exception as err:
    print('')
f.close





###################################################

import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
for i in ls:    
    data='id={}&type=1&city=32&state=1'.format(i).encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    d=r.urlopen(req).read().decode('utf-8','ignore')
f=open('./d.txt','w')
f.write(d+"\n")
f.close()
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
######################################    
    
    
f=open('./江苏文科.txt','w')
import urllib.request as r
url='file:./all_school.txt'
data=r.urlopen(url).read().decode('utf-8')
import re
c=re.compile('http://www.gaokaopai.com/daxue-jianjie-(.*?).html',re.S).findall(data)
b=re.compile('(.*?)http:/').findall(data)
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
for i in range(len(c)):
   data='id={}&type=1&city=32&state=1'.format(c[i])
   data1=data.encode()
   req=r.Request(url,data=data1,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
   d=r.urlopen(req).read().decode('utf-8','ignore')
   print('输出次数{}'.format(i))
   f.write(d+"\n")
f.close()
#########################################
m=[]
import urllib.request as r    
for i in range(2300):
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
    data='id={}&type=2&city=34&state=1'.format(ls[i])
    data=data.encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    p=r.urlopen(req).read().decode('utf-8','ignore')
    m.append(p)
    a=i
    print('输出{}次'.format(a))
########################################
#自动修改代码
for i in range(2300):
    a=m[i]
    if a.startswith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=2&city=34&state=1'.format(ls[i])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        p=r.urlopen(req).read().decode('utf-8','ignore')
        m[i]=p
    else:
        continue
#########################################################
m=[]
f=open('./江苏文科招生3.txt','w')
import urllib.request as r
url='file:./all_school.txt'
data=r.urlopen(url).read().decode('utf-8')
import re
c=re.compile('http://www.gaokaopai.com/daxue-jianjie-(.*?).html',re.S).findall(data)
b=re.compile('(.*?)http:/').findall(data)
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
for i in range(len(c)):
   data='id={}&type=1&city=32&state=1'.format(c[i])
   data1=data.encode()
   req=r.Request(url,data=data1,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
   d=r.urlopen(req).read().decode('utf-8','ignore')
   m.append(d)
   print('输出次数{}'.format(i))
   a=m[i]
   if a.startswith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=1&city=32&state=1'.format(c[i])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        d=r.urlopen(req).read().decode('utf-8','ignore')
        m[i]=d
   else:
       continue
   f.write(m+"\n")
f.close()   



#################################################
f=open('./all_school.txt','r',encoding='utf-8')
s=f.read()
import re
s1=re.compile('http://www.gaokaopai.com/daxue-jianjie-(.*?).html',re.S).findall(s)
s2=re.compile('.*?\t').findall(s)
for i in range(len(s1)):
    print('学校：{}学校代码：{}'.format(s2[i*2],s1[i]))
f.close()
m=[]
import urllib.request as r    
for i in range(2300):
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
    data='id={}&type=1&city=32&state=1'.format(s1[i])
    data=data.encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    p=r.urlopen(req).read().decode('utf-8','ignore')
    m.append(p)
    a=i
    print('输出{}次'.format(a))
#自动修改代码
for i in range(2300):
    a=m[i]
    if a.startswith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=1&city=32&state=1'.format(s1[i])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        p=r.urlopen(req).read().decode('utf-8','ignore')
        m[i]=p
    else:
        continue
f=open('./江苏文科.txt','w',encoding='utf-8')
for i in range(len(m)):
    p=m[i]
    f.write(p+"\n")
f.close()













##################################################
#最终版
f=open('./all_school.txt','r',encoding='utf-8')
s=f.read()
import re
s1=re.compile('http://www.gaokaopai.com/daxue-jianjie-(.*?).html',re.S).findall(s)
f.close()    
m=[]
import urllib.request as r    
for i in range(2300):
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
    data='id={}&type=1&city=32&state=1'.format(s1[i])
    data=data.encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    p=r.urlopen(req).read().decode('utf-8','ignore')
    m.append(p)
    a=m[i]
    if a.startswith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=2&city=34&state=1'.format(s1[i])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        p=r.urlopen(req).read().decode('utf-8','ignore')
        m[i]=p
    else:
        a=i
        print('{}次输出成功'.format(a))
        continue
f=open('./江苏文科.txt','w',encoding='utf-8')
for i in range(len(m)):
    p=m[i]
    f.write(p+"\n")
f.close()  
