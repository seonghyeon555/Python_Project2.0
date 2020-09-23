import urllib.request as request
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# src="http://www.aowuasia.com/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8")
# print(data)




src="https://data.tycg.gov.tw/api/v1/rest/datastore/f4ece141-4044-45bf-8a2d-2d1f1171dd74?format=json%22"
with request.urlopen(src) as response:
    data=json.load(response)
clist=data["result"]["records"]
with open("data.txt","w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["機關名稱"]+"\n")