'''
字符串常见的操作：
1.find 检测，字符是否包含在字符串中
2.count 返回出现的次数
3.replace 替换
4.split 分割
5.index 跟find作用一样，但会报异常
'''
'''
查找
find:检测某个子字符串是否包含在字符串中，如果在返回这个字符串开始位置的下标，否则就返回-1
find(子字符串，开始位置下标，结束位置下标)
#注意开始位置和结束位置可以省略，表示在整个字符串中查找
name = 'helloworld'
# print(name.find('o')) #4 表示第一个o的下标为4
# print(name.find('wor')) #6 表示找到的第一个w的位置为6
print(name.find('w',3))
print(name.find('w',8)) #-1 超出范围，返回-1
print(name.find('w',1,7)) #5
#包前不包后
'''
'''
2.index()
检测某个子字符串是否包含在字符串中，如果在返回这个字符串开始位置的下标，否则就会报错
index(子字符串你，开始位置下标，结束位置下标)
name = '大东北是我的家乡'
print(name.index('家'))  #6
print(name.index('家',4,6)) #ValueError: substring not found 范围小

'''
'''
3.count():
返回某个子字符串在整个字符串中出现的次数，没有就返回0
count(子字符串,开始位置，结束位置下标)
name='nimapuchi'
print(name.count('nimapuchi'))#1
print(name.count('i')) #2
print(name.count('i',1,3)) #1
#包前不包后
'''
'''
常见字符串的操作
capitalize 第一个字符大写
startswith 是否以某字符开头
endswith   是否以某字符结束
lower  大写字母转为小写
upper  小写字母转为大写



'''

