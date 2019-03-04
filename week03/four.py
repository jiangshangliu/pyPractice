#4．判断一个字符串是否为对称字符串（20分）用函数形式进行操作完成

def isEvenStr(str):
    if str == str[::-1]:   #判断是否对称
        return True
    else:
        return False

#调用函数
flag = isEvenStr("abcdedcba")
print(flag)
flag2 = isEvenStr("abcdetfyudcba")
print(flag2)