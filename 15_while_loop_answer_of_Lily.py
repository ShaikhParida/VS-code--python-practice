print("哈喽呀！我是一个求平均值的程序。")
total = 0
count = 0
user_input = input("（想结束输入请输入“q”）请输入数字：")
while user_input != "q":
    num = float(user_input)
    total += num
    count += 1
    user_input = input("（想结束输入请输入“q”）请输入数字：")

if count == 0:
    result = 0
else:
    result = total / count
print ("您输入的数字平均值为：" + str(result))