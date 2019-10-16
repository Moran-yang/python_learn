# is 与 == 的区别：is同时判断值和内存地址，==只判断值
a = 1
b = 1
print(id(a))
print(id(b))
if a is b:
	print('True', 'is')
else:
	print('False', 'is')

if a == b:
	print('True', '==')
else:
	print('False', '==')
	
	
a = [1,2,3]
b = [1,2,3]
print(id(a))
print(id(b))
if a is b:
	print('True', 'is')
else:
	print('False', 'is')

if a == b:
	print('True', '==')
else:
	print('False', '==')

import time
a = time.time()
l = [i for i in range(100)]
b = time.time()
print('耗时：%f' %(b-a))
