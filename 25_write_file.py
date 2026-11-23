# 写文件情况下，如果目标文件存在，则会自动清空目标文件的内容 所以'w'要慎用

# with open('./unknown.txt', 'w') as f:  # 写文件情况下，如果目标文件不存在，则会自动创建目标文件
#     f.write('Hello!Hello\n')           # 想实现需要手动加入换行符
#     f.write('Yoooooo')                 #
# print(open('./unknown.txt','r').read())


# 'w'和'a'模式下不能进行读操作f.read()会报错，'r+'才可以
with open('./unknown.txt', 'a', encoding = "utf-8") as f:  # 写文件情况下，如果目标文件存在，则可以用'a'避免自动清空目标文件的内容
    f.write('Hello!Hello\n')                               # 想实现需要手动加入换行符
    f.write('Yoooooo')                                     #
print(open('./unknown.txt','r').read())

#




