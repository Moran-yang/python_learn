# 解析：让你只需要一行代码就能生成列表、字典、集合，常与for循环结合

# 列表解析：
squares = [value**2 for value in range(1,11)] #range左闭右开
print(squares)

list1 = [i for i in range(1, 1000001)]
if min(list1) == 1:
    if max(list1) == 1000000:
        print('yes')
if min(list1) is 1:
    print('is 1')
    
# 错误写法：list2 = [j for j in range(1,21) and j%2 != 0 ] 条件不能写在for循环中，需要写在if里
list2 = [j for j in range(1,21) if j%2 != 0 ]
print(list2)

                                                                         
