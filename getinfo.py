import requests
import bs4
from bs4 import BeautifulSoup
import re
import os
import traceback




def getCurrInfo(fpath):
    try:
        bocurl = 'http://www.usd-cny.com/bankofchina.htm'
        html = getHTML(bocurl)
        infoDict = {}
        soup = BeautifulSoup(html, 'html.parser')
        currInfo = soup.find('div', attrs={'class': 'pp'})
        name = currInfo.find_all('a')[0]
        infoDict.update({'»õ±ÒÃû³Æ': name.text.split()[0]})

        keyList = currInfo.find_all('th')
        valueList = currInfo.find_all('td')
        keyList1 = currInfo.find_all('a')
        print('count country', len(keyList1))
        for i in range(len(keyList1)):
            key = keyList1[i].text
            val = valueList[i].text
            infoDict[key] = val

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(str(infoDict) + '\n')
    except:
        traceback.print_exc()

