import urllib.request as request
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url="https://www.ptt.cc/bbs/movie/index.html"
req=request.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
})
with request.urlopen(req) as response:
    data=response.read().decode("utf-8")

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div",class_="title")
with open("data3.txt", "w", encoding="utf-8") as file:
    for title in titles:
        if title.a != None:
            file.write(title.a.string+"\n")