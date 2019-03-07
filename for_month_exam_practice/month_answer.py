'''
随机农业图谱序列（46分）
（1）通过代码随机生成500个样本的arg序列（arg是由ABCD四个字母随机组成的），生成文件名为num.txt，
文件的具体格式如下[20分]：
S00001	  ABCD….CABD
S00002    CABD….BACD
S00003    BDCA….AABD
S00004    ADCB….ACBD
……………………………………………….
S00500    ABCD….AABC

（2） 编写一个函数，该函数有两个输入，一个为前面产生的arg.txt样本文件，
一个是某一个样本的编号（假定该样本的编号一定存在于dnData.txt中,例如S00003	ABACADAAABABTBTAACAC）；
函数输出一个文件，文件名为searchResult.txt。 searchResult.txt的格式和arg.txt的格式基本一致，
但是最后附加相似度数据项；
searchResult.txt样本数据的顺序需要按着和输入样本的相似度降序排序：（输入样本应该出现在第一行）[26分]。
例：S00001		ABCDACBTACBADACCTAB
    S00002		BBAGACDCABCCACADADCD
    S00003		ACADADBAATACCCBAABAB
两个序列的相似度为：两个序列中字母相同的个数。
样本S00002与样本S00001的相似度为11
样本S00003与样本S00002的相似度为8

        评分标准：
        ①样本编号必须连续，且从S00001到S10000（5分）
        ②样本的number序列的长度必须为20（5分）
        ③每个位置的 (A、B、C、D)必须随机生成（5分）
        ④按照格式将数据存入文件（5分）
        ⑤正确生成searchResult.txt文件（7分）
        ⑥searchResult.txt文件中的第一行应为输入样本（5分）
        ⑦searchResult.txt文件中应存在500条样本（5分）
        ⑧searchResult.txt文件中，先后按照降序排列（4分）
        ⑨求出并输出所有相似度的平均数（5分）
'''
import random
def get_str():
    s = ''
    a = 'ABCD'
    for i in range(20):
        b = random.choice(a)
        s+=b
    return s


with open('num.txt','w') as fp:
    for i in range(500):
        data = 'S'+str(i+1).zfill(5)+'\t'+get_str()+'\n'
        fp.write(data)


def f2():
    # 获取文件名和对比的数据的编号
    file_name = input("请输入文件名称：")
    s_id = input('请输入编号：')
    aList = []
    # 保存相似度的和
    sum = 0
    # 打开结果文件
    with open('searchResult.txt', 'w') as f:
        # 打开原始文件
        with open(file_name) as fp:
            # 读取原始文件
            data = fp.readlines()
            # 遍历原始文件的每一行
            for i in data:
                # 判断是否为对比的数据的编号
                # 取数要对比的数据
                if s_id in i:
                    # 6、⑥searchResult.txt文件中的第一行应为输入样本（5分）
                    f.write(i)
                    j = i.split('\t')[-1]
                    # 文件指针从头开始
                    fp.seek(0, 0)
                    # 比较相似度
                    for x in fp.readlines():
                        count = 0
                        y = x.split('\t')[-1]
                        for m in range(20):
                            if j[m] == y[m]:
                                count += 1
                        # 所有的相似度相加
                        sum += count
                        # 在原始数据后加上相似度
                        result_data = x.replace('\n', '\tcount=' + str(count) + '\n')
                        # 数据放到列表中
                        aList.append(result_data)
            # 按照相似度进行排序
            results_data = sorted(aList, key=lambda aStr: int(aStr[aStr.find('=') + 1:-1:]), reverse=True)
            # 往结果文件里一行行写入结果
            for mm in results_data:
                f.write(mm)
    # 9、⑨求并输出所有相似度的平均数（5分）
    avg = sum/500
    print(avg)


f2()
