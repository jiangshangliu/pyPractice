#一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

def perfectNum():
    for num in range(1,10000):
        s = 0
        for a in range(1,num):
            if not num%a:
               s += a
        if num == s:
            print('完美数：%d'%num)
perfectNum()

# import random
# list = list(random.randint(1,100) for i in range(9))
# print(list)


