'''
请使用Python完成以下功能：
一、随机DNA序列（共50分）
（1）使用代码随机生成20000个样本的DNA序列（DNA是由AGCT四个碱基对随机组成的），
生成文件名为dnaData.txt，文件的具体格式如下[25分]：
num00001	AGCTC TAGTT CGGTA TAACT
num00002    TTAGA ……… TAGCT
num00003    ATAGA ………AAGAT
num00004    ATAGG ……… CACTT
……………………………………………….
num20000    ATAGC ……… CTGAT
评分标准：
①样本编号必须连续，且从num00001到num20000（5分）
②样本的DNA序列的长度必须为20（5分）
③每5个序列间需要间隔1个空格，如num00001所示（5分）
④每个位置的氨基酸(A、G、C、T)必须随机生成（5分）
⑤按照格式将数据存入文件（5分）
'''

s1='ABCD'
# import random
# for i in range(1,501):
#     ss=''
#     for j in range(20):
#         ss+=random.choice(s1)
#     print('S'+str(i).zfill(5)+'\t'+ss+'\n')

#print(s1.partition('C'))  #按指定分隔符分割，返回 左边字串，分隔符，右边字串 的三部分的元组

#print('1'.rjust(3,'0'))  #返回指定长度的字符串 ，并右对齐，默认前面用空格填充，也可以指定字符

#print('1'.zfill(3))    #返回指定长度的字符串 ，并右对齐，前面用 “0” 填充



#循环字典来进行比较相同的数量
dict1 = {'S00001\tCCDBCBACACADACCBADBA': 0, 'S00002\tAAACBCDCCDCCDDCBDADD': 0, 'S00003\tCADADBDCDCDDDBBCABDD': 0, 'S00004\tCBBBABAABCCBBBDDCAAA': 0, 'S00005\tAAADDDDCBADDBBBBDADA': 0}
s2 =  'S00002\tAAACBCDCCDCCDDCBDADD'
for i in dict1.keys():
    count1=0    #计数
    for j in range(20):
        #判断比较
        print(i)
        print('i[-20:][%d]'%j,i[-20:][j])
        print('s2[-20:][%d]'%j,s2[-20:][j])
        '''
        核心代码，先进行截取操作，截取倒数第20个至末尾，此时结果是列表；
        然后通过下标获取该列表的对应元素，
        例如：i= "S00001   	CCDBCBACACADACCBADBA"  i[-20:][0] = 'C'
        '''
        if i[-20:][j]==s2[-20:][j]:
            count1+=1
    dict1[i]=count1
print(dict1)














