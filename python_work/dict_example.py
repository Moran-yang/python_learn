# 6-1人物信息
information = {
    'name': 'yangyang',
    'age': '22',
    'country': 'China'
    }
print(information)

# 遍历字典
for key, value in information.items():
    print('\n键为：' + key)
    print('\t值为：' + value)

for k, v in information.items():
    print('Her ' + k.title() + ' is ' + v.title() + '.')

for k in information.keys():
    print(k.title())


