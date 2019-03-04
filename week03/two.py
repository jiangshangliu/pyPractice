'''
2.读入文件‘monday.txt’.统计文件中每个单词的数量并且进行输出。
txt的文本文件为 Python is easy.Python is easy.Python is easy.
然后再将下面一段文字加入到Monday.txt中然后进行输出
‘张三 18 99分
 李四   23  97分
 王小六 26   67分
 二妮   37   45’
添加文字用函数进行添加
'''
def fileread():
    d = {}  #空字典
    list = [] #空列表
    with open('C:/Users/刘小川/Desktop/monday.txt','r') as f:
        con = f.read()
        con = con.replace('.',' ')  #替换.
        list = con.split(" ",con.count(' ')-1) #按空格切割   count-1次消除末尾空格
        for i in list:
            d[i] = list.count(i)   #统计文件中每个单词的数量
        print(d) #输出

def filewrite():
    str = '张三 18 99分  ' \
          '  李四   23  97分  ' \
          '  王小六 26   67分  ' \
          '  二妮   37   45'
    with open('C:/Users/刘小川/Desktop/monday.txt', 'a') as p:   #追加
        p.write(str)
        p.flush() #刷新
    with open('C:/Users/刘小川/Desktop/monday.txt', 'r') as d:   #读内容
        cont = d.read()
        print(cont)   #输出

#调用函数
fileread()
filewrite()



