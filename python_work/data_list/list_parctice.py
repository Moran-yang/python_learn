# 3-1 打印每个朋友的名字
names = ['yangyang', 'zhu', 'hu', 'qin', 'zhou']
print(names[0])

# 3-2 为每人打印一条消息，抬头为每个朋友的名字
for i in range(0, len(names)):
	message_greeting = names[i] + ", it's nice to meet you."
	print(message_greeting)

# 3-4 邀请至少3位嘉宾
names = ['yangyang', 'zhu', 'hu', 'qin', 'zhou']
for j in names:
	print("Invite " + j + " to join us")
# 3-5 修改嘉宾名单。有位嘉宾无法赴约，需另外邀请
cannot_come = 'yangyang'
print("\n" + cannot_come.title() + " cannot come") 

print("\nyangyang".title() )

# 3-6 添加嘉宾。指出找到更大的餐桌
print("I have found a bigger dinner table")
names.insert(0, 'zu')
names.insert(1, 'zuzu')
names.append('zuzuzu')
for i in names:
	print("Invite " + i + " to join us")

# 3-7 缩减名单，刚得知只能邀请两位
print("I am very sorry that we can only invete two")
#使用pop不断删除名单中嘉宾，直到只有两位为止
while len(names) > 2:
	popped_person = names.pop()
	print(popped_person + "I apologize for my carelessness, I cannot invite you for ...")
print(names)

for i in names:
	print(i + ", you are still invited")

#最后使用del将列表清空, 判断列表是否清空也可用len>0,但下面这种存在即非零的效率更高
while names:
	del names[0]
print(names)

