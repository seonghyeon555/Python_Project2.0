# # file=open("data.txt",mode="w",encoding="utf-8") #开启
# # file.write("好棒棒\n测试中文") #操作
# # file.close()#关闭
#
# with open("data.txt",mode="w",encoding="utf-8") as file:
#     file.write("5\n3")
#
#
# sum=0
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     for line in file:
#         sum+=int(line)
# print(sum)
import json
with open("config.json",mode="r") as file:
    data=json.load(file)

data["name"]="New Name" #修改变数的资料
with open("config.json",mode="w") as file:
    json.dump(data,file)
