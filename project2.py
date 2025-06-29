
'''

import requests
from bs4 import BeautifulSoup as bs
url = requests.get('https://invoice.etax.nat.gov.tw/')
url.encoding='utf-8'

soup = bs(url.text,'html.parser') #轉換成dom樹
td = soup.select('.container-fluid')[0].select('.etw-tbiggest')  # 取出中獎號碼的位置
ns = td[0].getText()  # 特別獎
n1 = td[1].getText()  # 特獎
n2 = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]] # 頭獎，因為存入串列會出現 /n 換行符，使用 [-8:] 取出最後八碼

print(td)
print()
print(ns)
print(n1)
print(n2)

while True:
    try:
        # 對獎程式
        num = input('輸入你的發票號碼：')
        if num == ns: print('對中 1000 萬元！')
        if num == n1: print('對中 200 萬元！')
        for i in n2:
            if num == i:
                print('對中 20 萬元！')
                break
            if num[-7:] == i[-7:]:
                print('對中 4 萬元！')
                break
            if num[-6:] == i[-6:]:
                print('對中 1 萬元！')
                break
            if num[-5:] == i[-5:]:
                print('對中 4000 元！')
                break
            if num[-4:] == i[-4:]:
                print('對中 1000 元！')
                break
            if num[-3:] == i[-3:]:
                print('對中 200 元！')
                break
    except:
        break
        
'''

'''

import requests
from bs4 import BeautifulSoup as bs

payload = {
'startStation' : '3300-臺中' ,
'endStation' : '1210-新竹' ,
'transfer' : 'ONE',
'rideDate' : '2025/06/09' ,
'startOrEndTime' : 'true' ,
'startTime' : '00:00' ,
'endTime' : '23:59' ,
'trainTypeList' : 'ALL'
}


url = requests.post('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime',data=payload)
url.encoding='utf-8'

print (url.text)

'''

from bs4 import BeautifulSoup as bs
html_sample = '\
<html> \
 <body> \
    <h1 id= "title">Hello World</h1> \
    <a href="#" class="link">This is link1</a> \
    <a herf="# link2" class="link">This is link2</a> \
 <body/> \
</html>'

soup = bs(html_sample, features="html.parser")
print(soup.select('html')[0])