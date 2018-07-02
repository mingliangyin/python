# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:48:02 2018
爬取百度网页数据，用http:// 而不是其他
题目十一：爬取百度网页数据
1.爬取百度搜索标题
2.爬取标题下的描述
3.搜索的标题的网站


@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=pythong&oq=r&rsv_pq=995c85c000009a8d&rsv_t=4eab5OvsPf8cuvz7nGhsxFrgN2w8RwJWSaosdlICUpNZxmUJzsUXFoW8Pew&rqlang=cn&rsv_enter=1&inputT=4496&rsv_sug3=15&rsv_sug1=19&rsv_sug7=100&rsv_sug2=0&rsv_sug4=4496'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls=re.compile('"title":"(.*?)"').findall(data)
ls1=re.compile('class="c-abstract">(.*?)</div>',re.S).findall(data)
ls2=re.compile('"url":"http://(.*?)"').findall(data)
for i in range(len(ls)):
    print('标题：{}'.format(ls[i]))
for i in range(len(ls1)):
    print('内容：{}'.format(ls1[i]))
for i in range(len(ls2)):
    print('网址：{}'.format(ls2[i]))
    
    
    
    
    
    
    
    
    
    
    



