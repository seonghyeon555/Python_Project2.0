import random
# data=random.sample([1,5,6,10,20],3)
# data1=random.choice([1,5,6,10,20])
# print(data)
# print(data1)
# data=[1,5,8,20]
# random.shuffle(data)
# print(data)

data=random.random()
print(data)

data1=random.uniform(60,100)
print(data1)

data2=random.normalvariate(100,10)
print(data2)

import statistics as stat
data3=stat.stdev([1,2,3,4,5,8,100])
print(data3)

lst = []
rep_lst = []   #重复数字
uniq_lst = []  #不重复数字
for i in range(10):
    temp = random.randint(1,20)   #产生随机数，闭区间
    if temp in lst and temp not in rep_lst:   #寻找重复数字
        rep_lst.append(temp)
    lst.append(temp)
for j in lst:
    if j not in rep_lst:
        uniq_lst.append(j)
print(lst)
print(len(rep_lst),':',rep_lst)
print(len(uniq_lst),':',uniq_lst)
