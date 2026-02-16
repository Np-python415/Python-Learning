'''
字典格式：
dic = {'name':'np','age':20)
注意：键值对形式保存，键具有唯一性，但值可以重复
字典名 = {键1：值1，键2：值2}
键值对形成保存，键与值:隔开，每个键值对之间，隔开
dic = {'name':'np','age':20}
print(type(dic))
#键具有唯一性
#重复后不会报错，前面的键名被后面覆盖
dic = {'name':'np','name':'kata'}
print(dic)
'''
'''
字典常见操作一：

1.查看操作：
1.1 变量名 [键名]
eg1:dic = {'name':'np','age':20}
# print(dic[2]) #不可以根据下标，字典中没有下标，查找元素需要根据键名，键名相当于下标
print(dic['name'])
1.2 变量名.get(键名)
dic = {'name':'np','age':20}
print(dic.get('name'))
print(dic.get('sex'))#不存在，返回None
print(dic.get('sex','不存在')) #没有这个键名，返回自己设置的默认值

2.修改元素:
通过key找到，即可修改
dic = {'name':'np','age':20}
dic['age'] = 100 #字典通过键名进行修改，列表通过下标进行修改
print(dic) #没有这个键名，返回自己设置的默认值

3.添加元素:
变量名['键'] = 数据不存在则新增
dic = {'name':'np','age':20}
dic['number'] = 181000000
print(dic) #没有这个键名，返回自己设置的默认值

4.删除元素:

del 删除整个字典 
del 字典名
dic = {'name':'np','age':20}
del dic
print(dic) #报错：NameError: name 'dic' is not defined

#删除指定的键值对
del 字典名[键]
dic = {'name':'np','age':20}
del dic['name']
print(dic) 

clear 清空整个字典，但保留了这个字典
字典名.clear()
dic = {'name':'np','age':20}
dic.clear()
print(dic)
#{}

pop 删除指定的键和值,键不存在就会报错
字典名.pop(键名)
dic = {'name':'np','age':20}
dic.pop('age')
print(dic)
'''
'''

'''

dic = {'name':'np','age':20}
dic.pop('age')
print(dic)
