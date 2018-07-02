# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:52:44 2018
练习六：获取淘宝数据并且展示(只要第一页的商品48个)
1.每一行显示4个商品信息(商品名，价格，付款，店铺名,地址，)
2.列出12排商品
3.给商品排序，从价格高到低
4.给商品排序，按照销量排序
5.商品过滤，只要15天退款的商品，包邮的商品

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E7%9F%AD%E8%A3%A4&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》mods 字典-》itemlist 字典-》data字典-》auctions 列表-》index 0 字典-》raw_title 变量
data['mods']['itemlist']['data']['auctions'][0]['raw_title'] #商品名
#data字典-》mods 字典-》itemlist 字典-》data字典-》auctions 列表-》index 0 字典-》view_price 变量
data['mods']['itemlist']['data']['auctions'][0]['view_price'] #价格
#data字典-》mods 字典-》itemlist 字典-》data字典-》auctions 列表-》index 0 字典-》view_sales 变量
data['mods']['itemlist']['data']['auctions'][0]['view_sales'] #付款
#data字典-》mods 字典-》itemlist 字典-》data字典-》auctions 列表-》index 0 字典-》nick 变量
data['mods']['itemlist']['data']['auctions'][0]['nick'] #商铺名
#data字典-》mods 字典-》itemlist 字典-》data字典-》auctions 列表-》index 0 字典-》item_loc 变量
data['mods']['itemlist']['data']['auctions'][0]['item_loc'] #地址

def mag(x):
        a=data['mods']['itemlist']['data']['auctions'][x]['raw_title']
        b=data['mods']['itemlist']['data']['auctions'][x]['view_price']
        c=data['mods']['itemlist']['data']['auctions'][x]['view_sales']
        d=data['mods']['itemlist']['data']['auctions'][x]['nick']
        e=data['mods']['itemlist']['data']['auctions'][x]['item_loc']
        print('商品名为：{}'.format(a))
        print('价格为：{}'.format(b))
        print('付款为：{}'.format(c))
        print('商铺名为：{}'.format(d))
        print('地址为：{}'.format(e))
mag(0)
mag(1)
mag(2)
mag(3)
mag(4)
mag(5)
mag(6)
mag(7)
mag(8)
mag(9)
mag(10)



