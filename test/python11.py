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
'''
li = ['one','two','three']
li.insert(2,'four')
print(li)
#['one', 'two', 'four', 'three']
#在指定位置插入元素，指定位置若有元素，那就会原有元素会后移