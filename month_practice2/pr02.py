'''
输入一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数。
'''
# s = input("请输入英文字母、空格、数字和其他字符：")
# dic = {'letter': 0, 'integer': 0, 'space': 0, 'other': 0}
# for i in s:
#     if i > 'a' and i < 'z' or i > 'A' and i < 'Z':
#         dic['letter'] += 1
#     elif i in '0123456789':
#         dic['integer'] += 1
#     elif i == ' ':
#         dic['space'] += 1
#     else:
#         dic['other'] += 1
#
# print('统计字符串：', s)
# print(dic)
# print('------------显示结果2---------------')
# for i in dic:
#     print('%s=' % i, dic[i])
# print('------------显示结果3---------------')
# for key, value in dic.items():
#     print('%s=' % key, value)

#------------------正则re.findall()------------------------------
import re
s = input('请输入一串字符：')
char=re.findall(r'[a-zA-Z]',s)#以列表类型返回全部能匹配的子串
num=re.findall(r'[0-9]',s)
blank=re.findall(r' ',s)
chi=re.findall(r'[\u4E00-\u9FFF]',s)#汉字的Unicode编码范围
other = len(s)-len(char)-len(num)-len(blank)-len(chi)
print('统计字符串：', s)
print('字母',len(char),'\n数字',len(num),'\n空格',len(blank),'\n中文',len(chi),'\n其他',other)

#---------------------正则re.match()--------------------------------
def splitFunc( ):
    tmpStr = input('请输入字符串：')
    charNum = 0
    digNum = 0
    spaceNum = 0
    otherNum = 0
    for i in range(len(tmpStr)):
        if re.match('[a-zA-Z]',tmpStr[i]):
            charNum +=1
        elif re.match('\d',tmpStr[i]):
            digNum +=1
        elif re.match('\s',tmpStr[i]):
            spaceNum +=1
        else:
            otherNum +=1
    print('字符：',charNum)
    print('数字：',digNum)
    print('空格：',spaceNum)
    print('其他：',otherNum)
splitFunc()

#-------------------内置函数------------------------
InPut = input('请输入字符串：')
letters  = [ ]
spaces = [ ]
digits   = [ ]
others = [ ]
for i in iter(InPut):
    if i.isalpha():
        letters.append(i)
    elif i.isspace():
        spaces.append(i)
    elif i.isdigit():
        digits.append(i)
    else:
        others.append(i)
print('''
字母: {}, 个数: {}
空格: {}, 个数: {}
数字: {}, 个数: {}
其他: {}, 个数: {}'''\
.format(letters, len(letters), spaces, len(spaces), digits, len(digits),others, len(others)))
