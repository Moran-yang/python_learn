# 为什么dict键值只能用不变类型

list = [1, 2]
print(id(list))
dict = {'green': list}
print(dict)
list[1] = 5
print(id(list))
print(dict)

#list最常用的操作就是改变其中一个元素，此时内存地址不变，
#dict键是静态，值是动态更新，所以只有值可以用list，键不行
#dimensions元组可以做键是因为dimensions（1）不合法，只能整个重新赋值，而整个赋值操作不常用，dimen还是静态的
