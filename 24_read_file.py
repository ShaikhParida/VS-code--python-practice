# 方法一 需要手动close
# f = open("./data.txt","r",encoding = "utf-8")
# content = f.read()
# print(content)
# f.close()

# 方法二 等效于方法一 with会自动关闭
# with  open("./data.txt","r",encoding = "utf-8") as f:
#     content = f.read()
#     print(content)

# 方法三 按照行打开
# with open("./data.txt","r",encoding = "utf-8") as f:
#     print(f.readline())
#     print(f.readline())

# 方法四
# with open("./data.txt","r",encoding = "utf-8") as f:
#     lines = f.readlines()    # 把lines里的储存到列表里
#     for line in lines:
#         print(line)

with open("./data.txt","r",encoding = "utf-8") as f:
    print(f.readlines())
