import urllib.request as request
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url="https://www.kookmin.ac.kr/home.php"
with request.urlopen(url) as response:
    data=response.read().decode("utf-8")

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
uls=root.find_all("ul",class_="notice-tab")
for ul in uls:
    print(ul.li.a.string)