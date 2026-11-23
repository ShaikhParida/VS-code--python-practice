# #open函数打开文件
# #open(文件的路径，模式，可选参数encoding="utf-8")


# #文件的三种读取方法

# #1
# f = open("./date.txt","r",encoding="utf-8")
# print(f.read()) # 会读全部的文件内容，并打印
# print(f.read()) # 会读取空字符串，并打印 （这是因为read函数会记录读取进度

# #2readline
# f = open("./date.txt","r",encoding="utf-8")
# print(f.readline()) # 会读取一行文件内容，并打印
# print(f.readline()) # 会读取一行文件内容，并打印

# f = open("./date.txt","r",encoding="utf-8")
# line = f.readline()      # 读第一行
# while line != "":        # 判断当前行是否为空
#     print(line)          # 不为空则打印当前行
#     line = f.readline()  # 读取下一行

# 3 readlines
# f = open("./date.txt","r",encoding="utf-8")
# lines = f.readlines()         # 把每行内容存储到列表里
# for line in lines:            # 遍历每行内容
#     print(line)               # 打印当前行

# 资源的释放与关闭
# f = open("./data.txt")
# print(f.read()) # 对文件的操作
# f.close()       # 使用close函数，关闭文件，释放资源
# 或者
# with open(open("./data.txt")) as f: # with调用 用完后文件会自动关闭
#     print(f.read())   # 对文件的操作
