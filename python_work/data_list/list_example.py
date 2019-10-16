# python中用[]表示列表，逗号隔开

# 访问列表元素，索引从0开始
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) #会显示包括方括号在内整个list
print(bicycles[0]) #trek
print(bicycles[0].title()) #变量名.功能 Trek
print(bicycles[-1]) #访问最后一个元素的特殊语法，类似还有-2， -3...

#使用列表中各个值
message = "my first bicycle was a " + bicycles[0].title() + "."
print(message)

#修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#添加列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

#对列表排序
bicycles.sort()
print(bicycles)
bicycles.reverse()
print(bicycles)


bicycles.sort(reverse=True)
print(bicycles)

# 无论是str型还是int型num都能排序
list1 = ['1', '2', '3', '4', '5']
list1.sort(reverse=True)
print(list1)
list2 = [1, 2, 3, 4, 5]
list2.sort(reverse=True)
print(list2)

# 列表切片
print(motorcycles)
print('The first three items in the list are: ' + str(motorcycles[0:3]))



