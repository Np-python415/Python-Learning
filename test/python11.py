'''
---------------列表------------
1.定义：
处理一组有序项目的数据结构。
2.格式：
列表名 = [元素1，元素2，元素3...]
注意：
1.列表的所有元素都放在一对中括号[]中，并使用逗号隔开。
2.一个列表中的数据类型可以不同。
li = [1,2,3]
print(li,type(li)) #[1, 2, 3] <class 'list'>
print(li[0]) #1
print(li[0:3])
#列表也可以进行切片操作
#列表是可迭代对象，可以for循环遍历取值
for i in li:
    print(i)
from operator import index
'''
'''
列表相关操作：
1.添加元素：
append
extend
insert
2.修改元素
通过下标修改
3.查找元素：
in
not in 
index
count
4:
删除元素：
del
pop
remove
5.排序：
sort
reverse
'''
'''
1.添加元素
append() extend() insert()
------------------------------
1.1 append():
li = ['one','two','three']
li.append('four')
print(li)
#['one', 'two', 'three', 'four']
#整体的添加
-------------------------------
1.2 extend():
li = ['one','two','three']
li.extend('four')
print(li)
#['one', 'two', 'three', 'f', 'o', 'u', 'r']
分散添加，逐一添加
-------------------------------
1.3 insert()
li = ['one','two','three']
li.insert(2,'four')
print(li)
#['one', 'two', 'four', 'three']
#在指定位置插入元素，指定位置若有元素，那就会原有元素会后移
'''
'''
2.修改元素
直接通过下标进行修改
li = [1,2,3]
li[2] = 'a'
print(li)
'''
''' 
3.查询
#index:返回指定数据的下标，如果不存在报错
#count:统计指定数据当前列表出现的次数
li = [1,2,3]
print(li.index(3)) #2
print(li.count(3)) #1
in:判断指定元素是否在列表中，若存在返回true，否否 false
not in:判断指定元素是否存在列表中，不存在返回True,存在返回False
li = ['a','b','c']
print('b' in li)
#True
#用户输入昵称，昵称重复则不能使用
#定义一个列表，保存已存在的昵称
while True:
    name_list = ['np', 'jh', 'cn', 'taylor']
    name = input("请输入您的名称：")
    # 判断名称是否已经存在
    if name in name_list:
        print(f"您输入的昵称{name}已经存在了")
    # 如果昵称不存在
    else:
        print(f"昵称被您使用了{name}")
        # 把昵称新增到列表中
        name_list.append(name)
        print(name_list)
        break
'''
'''
删除元素：
1.del
li = ['a','b','c']
#删除整个列表
#del li 
#根据下标删除元素
del li[0] 
print(li)
2，pop:删除指定下标的数据，python3版本删除最后一个元素
li = ['a','b','c']
li.pop() #删除最后一个元素
#['a', 'b']
li.pop(2) #不能指定元素删除，只能根据下标进行删除
print(li)
3.remove : 根据元素的值进行删除
li = ['a','b','c']
li.remove('c')
print(li)
#['a', 'b']
'''
'''
排序
1.sort:将列表按特定顺序重新排列，默认从小到大
li = [1,3,4,5,2,0]
li.sort()
print(li)
4.reverse()
#倒序将列表倒置
li = [1,3,4,5,2,0]
li.sort()
#[0, 1, 2, 3, 4, 5]
li.reverse()
# #[0, 2, 5, 4, 3, 1]
#[5, 4, 3, 2, 1, 0]
print(li)
'''
