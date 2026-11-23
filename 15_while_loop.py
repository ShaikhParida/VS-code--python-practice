# while 条件A:
#     行动B
# 条件A 持续为真 则 持续执行 行动B  循环判断
# 若 条件A 为假则退出循环

# 对比：
# for循环 有明确循环对象或次数
# while循环 循环次数为止

print("哈喽呀！我是一个求平均值的程序。")

i = 0
m = 0

user_input = input("（一次输入一个，想结束输入请输入“q”）\n请输入任意数量的数字：")

while user_input != "q":
    user_input = float(user_input)
    m = m + user_input
    i = i + 1
    user_input = input("（一次输入一个，想结束输入请输入“q”）\n请输入任意数量的数字：")

out = m/i
output = str(out)
print ("平均值为：" + output)
