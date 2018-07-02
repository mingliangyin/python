# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 09:19:32 2018
《当》动力火车
当山峰没有棱角的时候
当河水不再流
当时间停住日夜不分
当天地万物化为虚有
...
当太阳不再上升的时候
当地球不再转动
当春夏秋冬不再变换
当花草树木全部凋残

练习七:全球天气未来3天
1.使用多选其一，完成天气的提醒
2.一定要多ci使用到for循环,偶尔用一次while循环
3.初步学会使用debug，知道里面的设置断点，下一步执行，下一个断点执行。
4.《闪屏的制作》进入我们天气程序的时候，有一个温馨图形的提示。使用循环实现，
  要知道是什么意思，照抄网上代码不行。

    

@author: Administrator
"""
s='太阳不再上升'
if '太阳不再上升'==s:
    print('xxxx')

ls=['当山峰没有棱角的时候','当河水不再流','当时间停住日夜不分',
'当天地万物化为虚有']
print('wo' in ls)
print('当山峰没有棱角的时候' in ls)
#这种循环和列表很搭  
for line in ls:
    print(line)
    
ls=range(9)
for i in ls:
    print(i)

for i in range(0,9,1):
    print(i)

for i in range(0,9,2):
    print(i)

#固定次数的循环和列表和搭配
#还有一种循环，是没有次数限制的。有死循环，
for i in range(0,9999999999):
    print(i)

while True:#当什么时候
    print('kdlfjdkfjlkd')


############################
for i in range(1,101):
    print('跑第{}圈'.format(i))
    if i==3:
        break
    
for i in range(1,101):
    if i==10:
        print('幸运通道，执行进入下一次')
        continue
    print('跑第{}圈'.format(i))

###########
for i in [1,2,3]:
    print(i)
    for j in [0.1,0.2,0.3]:
        print(j)

"""
1------i
0.1----j
0.2----j
0.3----j
2------i
0.1----j
0.2----j
0.3----j
3------i
0.1----j
0.2----j
0.3----j
"""
#练习七
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》list列表-》index 0 字典-》main字典-》temp变量
data['list'][0]['main']['temp']
#data字典-》list列表-》index 0 字典-》main字典-》temp_max变量
data['list'][0]['main']['temp_max']
#data字典-》list列表-》index 0 字典-》main字典-》temp_min变量
data['list'][0]['main']['temp_min']

for i in range(8,30):
    a=data['list'][i]['dt_txt']
    b=data['city']['name']
    c=data['list'][i]['main']['temp']
    d=data['list'][i]['weather'][0]['description']
    e=data['list'][i]['main']['pressure']
    f=data['list'][i]['main']['temp_max']
    g=data['list'][i]['main']['temp_min']
    print('时间是{}，城市是{}，温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{},'
      .format(a,b,c,d,e,f,g))
    if (d=='多云'):
        print('今天天气晴朗，适合户外运动')
    elif (d=='小雨'):
        print('今天有小雨，不适合户外运动，出门记得带伞')
    elif (d=='晴'):
        print('今天天气晴朗，适合户外运动')
    elif (d=='中雨'):
        print('今天有中雨，不适合户外运动，出门记得带伞')
    else :
        print('今天天气阴，适合户外运动')



for i in range(11):
    if i==1:
        print(' '*6,'*'*3,'*'*3,' '*3)
    if i==2:
        print(' '*6,'*'*2,'欢'*1,'*'*2,' '*5)
    if i==3:
        print(' '*5,'*'*3,'迎','*'*3,' '*1)
    if i==4:
        print(' '*4,'*'*4,'使','*'*4,' '*3)
    if i==5:
        print(' '*5,'*'*3,'用','*'*3,' '*3)
    if i==6:
        print(' '*6,'*'*2,'天'*1,'*'*2,' '*5)
    if i==7:
        print(' '*5,'*'*3,'气','*'*3,' '*3)
    if i==8:
        print(' '*4,'*'*4,'管','*'*4,' '*3)
    if i==9:
        print(' '*5,'*'*3,'家','*'*3,' '*3)
    elif i==10:
        print(' '*6,'*'*3,'*'*3,' '*3)
 



 
  


#无聊话心形图
__author__ = 'taohao'  
import matplotlib.pyplot as plt  
from matplotlib import animation  
import numpy as np  
import math 
def drawHeart():  
    t = np.linspace(0, math.pi, 1000)  
    x = np.sin(t)  
    y = np.cos(t) + np.power(x, 2.0/3)  
    plt.plot(x, y, color='red', linewidth=2)  
    plt.plot(-x, y, color='red', linewidth=2)
    plt.xlabel('t')  
    plt.ylabel('h')  
    plt.ylim(-2, 2)  
    plt.xlim(-2, 2)
    plt.axis('off')
    plt.legend()  
    plt.show()  

drawHeart()









