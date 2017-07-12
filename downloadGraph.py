# -- coding: utf-8 --
import urllib.request
import requests
import re
import time
import os
from bs4 import BeautifulSoup

__url =  'http://fgowiki.com/guide/petdetail/%d'
__url1 = 'http://file.fgowiki.fgowiki.com/fgo/card/servant/%sA.jpg'
__url2 = 'http://file.fgowiki.fgowiki.com/fgo/card/servant/%sB.jpg'
__url3 = 'http://file.fgowiki.fgowiki.com/fgo/card/servant/%sC.jpg'
__url4 = 'http://file.fgowiki.fgowiki.com/fgo/card/servant/%sD.jpg'


for i in range(172,173):
    url = __url % i
    ii =str(i)
    if(i<10):
        ii = "00"+ii
    elif(i>=10 and i<100):
        ii = "0" +ii
    url1 = __url1 % ii
    url2 = __url2 % ii
    url3 = __url3 % ii
    url4 = __url4 % ii
    try:
        response = requests.get(url).content.decode('utf-8')
        soup = BeautifulSoup(response, 'lxml')
        figureInfo = soup.find_all(re.compile("script"), type="text/javascript")
        name = r'"NAME":"(.*?)"'
        name_original = re.findall(name, str(figureInfo))
        name_u8 = name_original[0].encode('latin-1').decode('unicode_escape')
        name = ii + name_u8
        route = r'D:\fgo\%s' % name
        os.mkdir(route)
        saveRoute1 = route + '\一破.jpg'
        saveRoute2 = route + '\二破.jpg'
        saveRoute3 = route + '\三破.jpg'
        saveRoute4 = route + '\满破.jpg'
        urllib.request.urlretrieve(url1, saveRoute1)
        urllib.request.urlretrieve(url2, saveRoute2)
        urllib.request.urlretrieve(url3, saveRoute3)
        urllib.request.urlretrieve(url4, saveRoute4)
        print(name)
    except:
        print("fail")


