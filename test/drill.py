#1.创建空的待办清单表
todo_list = []
#2.添加元素
# todo_list.append("学Python")
# todo_list.append("吃饭")
# todo_list.append("写项目")
todo_list.extend(["学Python","吃饭","写项目"])
# print("添加任务后：",todo_list)
#3.用pop删除最后一个任务
# todo_list.pop()
# print("删除最后一个任务后：",todo_list)
#4.用remove删除指定元素
# todo_list.remove("吃饭")
# print("remove删除指定任务:",todo_list)
#5.用切片取第一个任务
first_task = todo_list[0:1]
print("第一个任务（切片）:",first_task)
#6.遍历列表打印所有任务
print("最终待办清单：")
for task in todo_list:
    print("-",task)
#task:for循环的临时变量；列表里当前遍历到元素的起的名称
