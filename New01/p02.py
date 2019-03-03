#输入一个日期判断是这一年的第几天
def isHowday(year,month,day):
    p_year = [31,28,31,30,31,30,31,31,30,31,30,30]  #平年各月天数
    r_year = [31,29,31,30,31,30,31,31,30,31,30,30]  #闰年各月天数
    sum_day = 0
    str0 = str(year) +'年'+ str(month) +'月'+ str(day)+'日'  #字符串形式
    if (year % 4 ==0 and year % 100 != 0) or year % 400 == 0 :   #判断是否是闰年
        for i in range(0,month-1):              #加上第一个月到前一个月的总天数
            sum_day += r_year[i]
        print("%s是这一年的第%d天" %(str0,sum_day+day))
    else :
        for i in range(0,month-1):
            sum_day += p_year[i]
        print("%s是这一年的第%d天" %(str0,sum_day+day))
isHowday(2001,12,31)  #调用函数