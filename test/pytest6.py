'''
---------------3.三目运算符------------
为真结果 if 判断条件 else 为假结果
基本格式：
if-else
if-elif
if-elif-else
'''
'''
if-else
基本格式：
if 条件:
    满足条件时要做的事情
else:
    不满足条件时要做的事情
    
a = input("请输入：")
if a == '999':
    print("恭喜你答对了！")
else:
    print("很抱歉没答对！")

'''
'''
if-elif 结构 多选一
if-else 结构 二选一 
if 条件一:
   满足条件一要做的事情1
elif 条件2:
    满足条件2做的事情
elif 条件3:
     满足条件3做的事情
score = 88
if 85 <= score <= 100:
    print("优秀")
elif 60 <= score <=80 :
    print("及格")
elif 0<= score <=60:
    print("不及格")
   
'''
'''
if 嵌套
if 嵌套的基本格式
含义：if 里面有 if
注意：外层的if判断 ，也可以是if-else:
     内层的if判断 ，也可以是if-else。
格式：
if 条件1:
   事情1
   if 条件2 :
      事情2
else:
    不满足条件
#定义一个布尔型变量，表示是否有车票
ticket=True #True代表有车票，False 代表无车票
temp = 36.5 #正常人腋下体温36.3-37.2
if ticket == True:#外层if判断
    print("可以进站了-->",end="")
    # 正常人腋下体温36.3-37.2
    if 36.3 <= temp <= 37.2:
        print("体温正常，可以安心回家")
    else :
        print("您的体温异常")
else:
    print("您没有票不能进站")
'''
