'''
if 判断
运算符
if-else
if 嵌套

'''
'''
if
基本格式：
if 要判断的条件:
   条件成立要做的事情。
   #用户从控制台输入成绩，如果满分，输出"你真棒！",如果60分，输出”还要继续加油哈！"
score=input("请输入您的成绩：")
if score == '100':
    print("你真棒！")
if score == '60' :
    print("还要继续加油哈！")
'''
'''
运算符：
----------------1.比较运算符 关系运算符-------
== != > < >= <=
# a=99
# b=88
# print(a>b)
# 输出：True
# if a > b :
# print("a小于b")

---------------2.逻辑运算符------------------
and（与） or(或) not（非）
and 左右两边都符合才为真
a='嘿嘿'
b='嘻嘻'
if a == '嘿嘿' and b == '嘻嘻' :
    print('a和b都相等')
fruit = 'banana'
if fruit == 'banana' or fruit == 'apple' :
    print("带回来了")

'''

