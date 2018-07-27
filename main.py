"""
@author: mirrorChen
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: main.py
@time: 2018/7/27 9:05
@desc:
"""


from requests_html import HTMLSession
import requests
session = HTMLSession()
r=session.get("https://www.hao123.com/")
all_links=r.html.links
print(all_links)
#all_absolute_links = r.html.absolute_links
#print(all_absolute_links)
print("--"*30)
#抓取科技圈最新新闻
r=session.get("https://news.cnblogs.com/n/recommend")
# 通过CSS找到新闻标签
news = r.html.find('h2.news_entry > a')
for new in news:
    print(new.text)  # 获得新闻标题
    print(new.absolute_links)  # 获得新闻链接


# 保存图片到当前目录pics/win4000/目录
def save_image(url, title):
    img_response = requests.get(url)
    with open('./pics/win4000/'+title+'.jpg', 'wb') as file:
        file.write(img_response.content)
        file.close()

# 背景图片地址，这里选择1920*1080的背景图片
url = "http://www.win4000.com/wallpaper_2358_0_10_1.html"

session = HTMLSession()
r = session.get(url)

# 查找页面中背景图，找到链接，访问查看大图，并获取大图地址
items_img = r.html.find('ul.clearfix > li > a')
for img in items_img:
    img_url = img.attrs['href']
    if "/wallpaper_detail" in img_url:
        r = session.get(img_url)
        item_img = r.html.find('img.pic-large', first=True)
        url = item_img.attrs['src']
        title = item_img.attrs['title']
        print(url+title)
        save_image(url, title)
    else:
        print("get nothing from win4000")
print("OK!")





