import requests
import os
import time
import re
import traceback
from bs4 import BeautifulSoup

def getHTML(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}  # 模拟浏览器
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.raise_for_status())
        return r.text
    except:
        return "error connection"


def getCurrInfo(fpath):
        try:
            bocurl ='http://www.usd-cny.com/bankofchina.htm'
            html = getHTML(bocurl)
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            currInfo = soup.find('div', attrs={'class': 'pp'})
            name = currInfo.find_all('a')[0]
            infoDict.update({'货币名称': name.text.split()[0]})

            keyList = currInfo.find_all('th')
            valueList = currInfo.find_all('td')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
        except:
            traceback.print_exc()
            



def main(inurl):
    url = inurl
    root = "E:/college/chengxusheji/"
    path = root + time.strftime('%Y&%m&%d&%M', time.localtime(time.time())) + '.txt'  # 如果已经有当天的数据就要删掉重新存
    flag = 0
    outputfiles = 'e:/college/chengxusheji/currinfo.txt'
    getCurrInfo(outputfiles)
    try:
        kv = {'user-agent': 'Mozilla/5.0'}  # 模拟浏览器
        d = requests.get(url, timeout=30, headers=kv)
        d.raise_for_status()
        d.encoding = d.apparent_encoding
        if d.status_code == 200:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                with open(path, 'wb') as f:
                    f.write(d.content)
                    f.close()
                    flag = 1
                    print("file saved successfully")
            else:
                flag = 1
                print("the file is alredey exist")
    except:
        flag = 0
        print("error connection")
    print(flag)
    try:
        if flag == 1:
            with open('E:/college/chengxusheji/list.txt', 'w+') as li:
                li.write(str(path))
                li.close
                print("the list is update")
        else:
            print("the list already exist")
    except:
        print('cannot save')


# getHTML("http://www.usd-cny.com/bankofchina.htm")
main("c")

# if r.status_code==200:
#    r.encoding='utf-8'
#    print(r.text)
#    print(type(r))
#    print(r.headers)
