'''
for 循环（迭代循环）
作用：可以完成循环的功能，依次取出对象中的元素。
基本格式：
for 临时变量 in 可迭代对象:
    循环体
注意：冒号和缩进必须注意！！！
str = 'hellopython' #定义一个字符串
for i in str: # i是临时变量，可以随便写，i是常规写法
    print(i)
# 输出：
# h
# e
# l
# l
# o
# p
# y
# t
# h
# o
# n
3.2 range()
用来记录循环次数，相当于一个计算器
range(start,stop,step)#range里面的参数
#遵循包前不包后原则 [) 1<=x<5
#range() 里面只写一个数，这个数就是循环的次数，默认从0开始
#写两个数前面开始位置，后面结束位置

for i in range(1,5):
    print(i)
#for循环计算1+2+3...100
s = 0 #定义一个变量
for i in range(1,101):
    s += i
print("计算结果：",s)
i = 1
s= 0
while i<= 100:
    s += i
    i += 1
print("计算结果是：",s)
'''
'''
break和continue
break:中途退出 结束循环
continue: 结束当前循环，进入下一循环
#都是专门在循环中使用的关键字
# i = 1
# if i <= 5:
#     print("我在吃苹果")
#     break
#break' outside loop ;break和continue只能放在循环内部
作用：满足某一条件后退出
i = 1
while i<=5:
    print(f"小红在吃第{i}个苹果")
    if i == 3:
        print("吃饱了")
        break
    i += 1
'''
'''
continue
作用：退出本次循环，下一次循环继续
i = 1
while i<=5:
    print(f"小明在吃第{i}个苹果")
    if i == 3 :
        print(f"吃到了一条大虫子，第{i}个苹果不吃了")
        #在continue 之前，一定要修改计算器，否则会死循环
        i += 1
        continue
    i += 1
for i in range(5):
    if i == 3:
       # break
       continue
    print(i)
# break:打印：
# 0
# 1
# 2
#continue打印：
# 0
# 1
# 2
# 4
#总结：break 遇3 后不打印； continue 遇3后跳过3 继续打印

'''
