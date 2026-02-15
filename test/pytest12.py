'''
1.元组
元组基本格式：
tua = (1,2,3)
#定义元组时，如果只有一个元素，末尾要加逗号，多个元素用，隔开。
# tua = (1,2,3)
# print(type(tua))
#<class 'tuple'>
tua = (1,)
print(type(tua))
元组与列表的区别：
1.元组只有一个元素，末尾必须加一个逗号，列表不用
2.元组支持查询工作，不支持增删改
tua = (1,2,3)
print(tua[2]) #有下标，查询元素
count () index()
tua = (1,2,3,4,5,6)
print(tua.index(2))
print(tua.count(2))
print(len(tua)) #长度
#切片操作
tua = (1,2,3,4,5,6)
print(tua[1:])
#(2, 3, 4, 5, 6)
------------------应用场景：------------
函数的参数和返回值
格式化输出后面的（）本质上就是一个元组
name = 'np'
age = 20
print("%s的年龄是：%d" %(name,age))
info = (name,age)
print("%s的年龄是：%d" %(name,age))
'''
