# # class Point:
# #     def __init__(self,x,y):
# #         self.x=x
# #         self.y=y
# # p1=Point(3,4)
# # print(p1.x,p1.y)
# # p2=Point(5,6)
# # print(p2.x,p2.y)
#
# class FullName:
#     def __init__(self,first,last):
#         self.first=first
#         self.last=last
# name1=FullName("O.","William")
# print(name1.first,name1.last)
#
# name2=FullName("T.Y","Lin")
# print(name2.first,name2.last)

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def show(self):
#         print(self.x,self.y)
#     def distance(self,targetX,targetY):
#         return (((self.x-targetX)**2)+((self.y-targetY)**2))**0.5
# p=Point(3,4)
# p.show()
# result=p.distance(0,0)
# print(result)

class File:
    def __init__(self,name):
        self.name=name
        self.file=None
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8")
    def read(self):
        return self.file.read()
f1=File("data.txt")
f1.open()
data=f1.read()
print(data)


f2=File("data2.txt")
f2.open()
data=f2.read()
print(data)
