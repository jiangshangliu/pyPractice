'''（1）通过代码随机生成1000个样本的arg序列（arg是由ABCD四个字母随机组成的），生成文件名为num.txt，文件的具体格式如下[20分]：
S00001	  ABCD….CABD
S00002    CABD….BACD
S00003    BDCA….AABD
S00004    ADCB….ACBD
……………………………………………….
S00500    ABCD….AABC
'''
import random

#写入并生成随机样本
arg=open('C:/Users/刘小川/Desktop/num.txt','w')
s1='ABCD'
for i in range(1,501):
    ss=''
    for j in range(20):
        ss+=random.choice(s1)
    arg.write('S'+str(i).zfill(5)+'\t'+ss+'\n')   #核心代码
    #返回指定长度字符串，并右对齐，前面使用‘0’填充

    #刷新和关流
arg.flush()
arg.close()

'''（2）编写函数从num.txt生成的500条数据中随机取出一条例如S00003	  ABACADAAABABTBTAACAC）；
和生成的1000条数据进行一一比对，但是最后附加相似度数据项；  
输出一个文件，文件名为searchResult.txt ；
样本数据的顺序需要按着和输入样本的相似度降序排序：（输入样本应该出现在第一行）[26分]
'''


# 读出并随机生成样本
def similarity():
    arg = open('C:/Users/刘小川/Desktop/num.txt', 'r')
    # 读取所有行存入列表  ['S00001\tCCDBCBACACADACCBADBA\n',...]
    list1 = arg.readlines()

    # 随机抽取一行内容  s2 S00316	BCCBCABCAAACDBCCDCCC
    s2 = list1[random.randint(0, 499)]
    arg.close()

    # 读出并循环去掉换行
    arg = open('C:/Users/刘小川/Desktop/num.txt', 'r')
    # 创建空字典存储
    dict1 = {}
    for i in arg:
        i = i.replace('\n', '')
        dict1[i] = 0
        # dict1: {'S00001\tCCDBCBACACADACCBADBA': 0, ...}
    arg.close()

    # 循环字典来进行比较相同的数量
    for i in dict1.keys():
        count1 = 0  # 计数
        for j in range(20):
            # 判断比较
            '''
               核心代码，先进行截取操作，截取倒数第20个至末尾，此时结果是列表；
               然后通过下标获取该列表的对应元素，
               例如：i= "S00001   	CCDBCBACACADACCBADBA"  i[-20:][0] = 'C'
            '''
            if i[-20:][j] == s2[-20:][j]:
                count1 += 1
        dict1[i] = count1

    # 倒序排序
    list2 = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
    # list2:  ( ('S00333\tCCAABACACCDCDBDCDCCA', 12),('S00160\tACBABCDACBBADDCCBCCD', 11) )

    # 写入到新的文件中
    arg1 = open('C:/Users/刘小川/Desktop/searchResult.txt','w')
    arg1.write(s2)  # 输入样本应该出现在第一行
    for i in list2:
        print(i)
        arg1.write(str(i[0]) + '\t' + str(i[1]) + '\n')
        arg1.flush()
    arg1.close()
    print('结束！')

#调用函数
similarity()