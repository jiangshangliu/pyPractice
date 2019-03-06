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
    # 9、⑨求出并输出所有相似度的平均数（5分）
    avg = sum/500
    print(avg)


f2()
