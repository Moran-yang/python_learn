names = ['yang', 'zhu', 'hu', 'qin', 'zhou']	
names[1] = '1'
print(names)
names[1] = ['2'] #此时替换'zhu'为列表['2']
print(names)
print(type(names))
print(type(names[1])) #list类型
print(type(names[2])) #str类型



#最后使用del将列表清空，方法1：存在即不为0，方法2：len>0
list = ['1', '2', '3', '4', '5']
while list:
	del list[0]
print(list) # [] while 一个个删最后不会返回内存空间
if list:
	del list # del list是删除整个列表，返回了内存空间
print(list)

