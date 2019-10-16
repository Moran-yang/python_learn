# 字符串大小写设定
name = "Eric hellon"
print(name.title()) 
print(name.lower()) 
print(name.upper()) 


# 单引号与双引号的使用
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

#+号可以联接字符串
famous_person = "Albert Einstein"
message = '"A person who never made a mistake never tried anything new."'
print(famous_person + " once said, " + message)

# 去掉字符串前后或所有空格
famous_person = "\t Albert \nEinstein "
print(famous_person)
print(famous_person.lstrip())
print(famous_person.rstrip())


#数字给变量赋值，与字符串联接时需要申明其数据类型
volue = 8
message = "my favorite number is " + str(volue) #flod浮点数
print(message)
