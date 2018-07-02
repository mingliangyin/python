# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 14:24:06 2018
文件存储的问题，文件读取，文件操作
保存一个文本文件的操作过程：
1.打开记事本
2.写入内容
3.另存为
4.选择路径
5.写文件名
6.设置文件格式encoding
7.保存
读取文件的操作过程：
1.找到文件的路径和位置
2.双击打开

第七题：保存淘宝数据(小组项目)
1.每个组员爬取100页数据(同一种商品)，条件是北京，上海，广州，成都...
2.保存的商品信息有(同第六题),并且是以为csv格式保存
3.单个组员求出当前城市的商品的众数(最多的价格)
4.小组文件合并，求出商品的平均价格

@author: Administrator
"""
f=open('./a.txt','r')#ctrl+i
print(f.readline())
print(f.readline())

f=open('./a.txt')
s=f.read()#讲所有文本读取到一个字符串当中去
ls=f.readlines()#将所有的文本中的每行读取到一个列表中去
for line in ls:
    print(line)

                 #encoding 文件的格式
f=open('./a.txt','r',encoding='gbk')#ctrl+i
print(f.readline())
print(f.readline())
####################################写文件
f=open('./b.txt','w',encoding='utf-8')
f.write(' 辛德勒的名单 \n后窗')
f.write('  好家伙 \n 惊魂记')
f.close()#关闭文件，保存文件

f=open('./c.csv','w')#csv表格文件，以逗号分割
f.write('辛德勒的名单,后窗,呼啸山庄\n')
f.write('好家伙,惊魂记,简爱\n')
f.close()#关闭文件，保存文件

f=open('./c.csv','w')#csv表格文件，以逗号分割
for i in range(1000):
    f.write("{},{}\n".format(i,'我'))
f.close()#关闭文件，保存文件

#打开记事本
import os
os.system('notepad')

#练习七

b=0
f=open('./qunzi.csv','w',encoding='utf-8')
f.write('序号,店铺名,商品名,价格,销量,地址\n')
for i in range(0,100):
    import urllib.request as r
    url2='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180621&loc=%E6%B8%A9%E5%B7%9E&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=0&ajax=true'
    a=44*i
    url=url2.replace('0&ajax=true',str(a)+'&ajax=true')
    data=r.urlopen(url).read().decode('utf-8')
    import json
    data=json.loads(data)
    l=len(data['mods']['itemlist']['data']['auctions'])
    for a in range(0,l):
        nick=data['mods']['itemlist']['data']['auctions'][a]['nick']#店铺名
        raw_title=data['mods']['itemlist']['data']['auctions'][a]['raw_title']#商品名
        view_price=data['mods']['itemlist']['data']['auctions'][a]['view_price']#价格
        view_sales=data['mods']['itemlist']['data']['auctions'][a]['view_sales']#销量
        item_loc=data['mods']['itemlist']['data']['auctions'][a]['item_loc']#地址
        b=b+1
        f.write('{},{},{},{},{},{}\n'.format(b,nick,raw_title,view_price,view_sales,item_loc))
    print('第{}页已获取数据'.format(i+1))
f.close()
print('关键词为“裙子”温州地区前100页数据获取完成')


















