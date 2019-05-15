import requests
import os
import time
import re
import traceback
from bs4 import BeautifulSoup
import bs4
import csv


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
        url = 'http://www.usd-cny.com/bankofchina.htm'
        html = getHTML(url)
        infoDict = {}
        val = []

        soup = BeautifulSoup(html, 'html.parser')
        currInfo = soup.find('div', attrs={'class': 'pp'})
        # name = currInfo.find_all('a')[0]
        # infoDict.update({'货币名称	汇买价	钞买价	汇卖价	钞卖价	折算价': ' '})
        infoDict.update()

        valueList = currInfo.find_all('td')
        keyList = currInfo.find_all('a')
        list = [[0] * 6 for i in range(len(keyList))]
        ilist =[]
        print('count country', len(keyList))  # 国家货币总数
        for i in range(len(keyList)):
            key = keyList[i].text
            # val = valueList[6*i+1].text + ' ' + valueList[6*i+2].text + ' ' + valueList[6*i + 3].text + ' ' + valueList[6*i+ 4].text + ' ' + valueList[6*i+5].text
            val = valueList[6 * i + 1].text + '\n ' + valueList[6 * i + 2].text + '\n' + valueList[
                6 * i + 3].text + '\n' + valueList[6 * i + 4].text + '\n' + valueList[6 * i + 5].text
            infoDict[key] = val

        for i in range(len(valueList)):
            ilist.append(valueList[i].string)


        for i in range(0, len(keyList), 1):
            list[i] = ilist[6 * i:6 * i + 6]
        print(list[0])

        try:
            with open(fpath, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["货币名称", "汇买价", "钞买价", "汇卖价", "钞卖价", "折算价"])
                writer.writerows(list)  

        except:
            print('csvfile save failed.')

    except:
        traceback.print_exc()




def main(inurl):
    url = inurl
    root = "e:/homework/python/pydata/"
    path = root + time.strftime('%Y&%m&%d&%M', time.localtime(time.time())) + '.txt'  # 如果已经有当天的数据就要删掉重新存
    flag = 0
    outputfiles = root + 'currinfo' + time.strftime('%Y&%m&%d&%M', time.localtime(time.time())) + '.csv'
    getCurrInfo(outputfiles)
    # write_csv_file(outputfiles, ['货币名称','汇买价','钞买价','汇卖价', '钞卖价', '折算价'], list)


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
                    flag = 1  # 成功下载新数据，就要更新目录
                    print("file saved successfully")
            else:
                flag = 1
                print("the file is alredey exist")
    except:
        flag = 0
        print("error connection")
    print(flag)
    try:
        if flag == 1:  # 成功下载，需要删除旧数据
            with open('e:/homework/python/pydata/list.txt', 'r') as li1:
                removptr = li1.read()
                print(removptr)
                os.remove(removptr)
                print("the outdate file is delete")
        else:
            print("the list already deleted")
    except:
        print('cannot delete')
    try:
        if flag == 1:
            with open('D:/homework/python/pydata/list.txt', 'w+') as li:
                li.write(str(path))
                li.close
                print("the list is update")
        else:
            print("the list already exist")
    except:
        print('cannot save')


# getHTML("http://www.usd-cny.com/bankofchina.htm")
main("http://www.usd-cny.com/bankofchina.htm")

# if r.status_code==200:
#    r.encoding='utf-8'
#    print(r.text)
#    print(type(r))
#    print(r.headers)
