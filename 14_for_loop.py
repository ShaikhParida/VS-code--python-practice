# for 变量名 in 可迭代对象：列表、字符、字符串
#    # 对每个变量做一些事情
#    # ...

# temperature_dict = {"111":36.4, "112":36.6, "113":36.2}
# temperature_dict.keys()      # 所有键
# temperature_dict.values()    # 所有值
# temperature_dict.items()     # 所有键值对

# 检查所有员工体温代码：
# for staff_id,temperature in temperature_dict.items():
#     if temperature >= 38:
#         print(staff_id),
#         print(temperature)
#         print("\n")

#     等价于

# for temperature_tuple in temperature_dict.items():
#     staff_id = temperature_tuple[0]
#     temperature = temperature_tuple[1]
#     if temperature >= 38:
#         print(staff_id),
#         print(temperature)
#         print("\n")

# range表示整数序列 range(5, 10)等价于[5,6,7,8,9]
# range还可以加上步长 range(起时值, 结束值, 步长）
# 序列内不包括结束值
# range(5, 10, 2)等价于[5, 7, 9]

total = 0
for i in range(1, 101):
    total = total + i

print(total)