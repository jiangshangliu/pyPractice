#3. 生成一个有10个数的随机数组，判断每个数字出现的次数
def num():
    import random
    list = []  #存储数字
    d = {}  #统计次数
    for i in range(10):
        list.append(random.randint(1,50))
    print(list)
    for i in list:
        d[i] = list.count(i)
    print('各数字出现次数：',d)  #输出次数

#调用函数
num()