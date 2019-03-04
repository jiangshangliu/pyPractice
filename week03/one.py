#1.生成20个范围在1-200的整数，并且能够打印输出？

def printNum():
    import random
    for i in range(20):
        print("%d:"%(i+1),random.randint(1,200))  #输入序列号和数字

printNum()   #调用函数

