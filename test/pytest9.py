'''
1.字符串编码
2.字符串常见操作
3.列表
4.列表的相关操作
'''
'''
字符串编码常用种类
编码          作用      所占字节数
ASCII        表示英语及西欧语言   8bit/1bytes
GB2312        国家简体中文字符集，兼容ASCII 2bytes
Unicode       国际标准组织统一标准字符集 2bytes
GBK           GBK2312的扩展字符集  2bytes
UTF-8         不定长编码      1-3bytes  
'''
''''
字符串编码
本质上就是：二进制与语言文字的一一对应关系。

Unicode:所有字符都是2个字节，
优点：字符与数字之间转换速度快
缺点：占用空间大

UTF-8：更精准，对不同字符用不同的长度表示
优点：节省空间
缺点：字符与数字之间转换速度慢，每次都需要计算字符用多少个字节来表示。
'''
'''
字符串编码转换：
1.编码：encode()
将其他的编码字符串转换成Unicode编码。
2。解码：decode()
将Unicode的编码字符串转换成其他的编码的字符串。
a = 'hello'
print(type(a))
#<class 'str'>   str:字符串是以字符为单位进行处理
a1 = a.encode()
print("编码后：",a1)
print(type(a1))
#<class 'bytes'>
a2 = a1.decode()
print("解码后：",a2)
print(type(a2))
#<class 'str'>
st = "这里是大美中国"
st1 = st.encode("utf-8")
print(st1,type(st1))
st2 = st1.decode("utf-8")
print(st2,type(st2))
'''
'''
字符串运算符
+ 字符串连接            a + b 输出结果：HelloPython
* 重复输出字符串         a*2 输出结果：HelloHello
[] 通过索引获取字符串字符  a[1]输出结果e
[:]截取字符串的一部分      a[1:4] 输出结果 ell
in 成员运算符-如果字符串中包含给定的字符返回True 'H' in a 输出结果True
not in 成员运算符-如果字符串中不包含给定字符返回True 'M' not in a 输出结果 True
'''
'''
+ : 字符串拼接
name1 = '大美'
name2 = '中国'
print(name1+name2)
#大美中国
* : 重复
name = "我爱中国"
print(name*6)
print("我爱中国\n"*5)

'''
'''
常见字符串操作：
成员运算符作用：检查字符串中是否包含了某个子字符串（即某个字符或多个字符）
# 1. in ：如果包含返回True
# 2. not in :如果不包含，返回True ,包含返回False
name = 'np'
print('p' in name)
#返回 True
print('m' in name)
#返回 False
print('p' not  in name)
#返回 False
print('m' not in name)
#返回True

'''
'''
下标/索引
Python中下标从0开始
写法：字符串名[下标值]
#注意：从右往左数，下标是从-1 开始，-1，-2,-3...
作用：通过下标能够快速找到对应的数据
name = 'nimapuchi'
#从左往右数，下标从0开始
print(name[0])#n
print(name[3])#a
print(name[9]) #IndexError: string index out of range 超出下标范围
#从右往左数，下标从-1开始 -1.-2 ....
name = 'nimapuchi'
print(name[-1])
print(name[-2])
'''
'''
切片：
含义：指对 操作的对象截取其中一部分的操作
语法：[开始位置：结束位置：步长]
包前不包后的原则：即从起始位置开始，到结束位置的前一位结束（不包含结束位置）
st = 'ABCDEFGHIJK'
print(st[0:3]) #ABC
print(st[3:7]) #DEFG
print(st[3:])  #DEFGHIJK 下标为3之后的全部截取到
print(st[:4])  #ABCD 下标为3之前的全部截取到，不包含4
#从右往左
st = 'ABCDEFGHIJK'
# print(st[-1:]) #K
# print(st[:-1]) #ABCDEFGHIJ
# print(st[-1:-5])
----------- 步长:表示选取间隔，不写步长，则默认是1-------------
# 步长的绝对值大小决定切取的间隔，正负好决定切取方向
# 正数：从左往右
# 负数：从右往左
# print(st[-1::1]) #K
# print(st[-1:-5:-1])
'''
