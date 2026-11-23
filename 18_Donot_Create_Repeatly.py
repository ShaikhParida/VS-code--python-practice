# # 造轮子
# def median(num_list):
#     sorted_list = sorted(num_list) #数组排列函数
#     n = len(sorted_list)
#     #如果一共有奇数个数字，则取中间那个
#     if n % 2 == 1:
#         return sorted_list[n // 2] # 向下取整
#     # 如果一共有偶数个数字，取中间那两个的平均值
#     else:
#         return (sorted_list[n // 2] + sorted_list[n // 2 - 1]) / 2
#
# print(median([69,124,-32,27,217]))

# 等价于

# import statistics
# print(statistics.median([69,124,-32,27,217]))

# 三种引入模块
# import语句、from...impport...语句、from...import *

from statistics import median, mean
print(median([19,-5,36]))
print(mean([19,-5,36]))





