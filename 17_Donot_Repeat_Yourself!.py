# def calculate_sector (central_angle, radius):
#     # 接下来是一些定义函数的代码
#     sector_area = central_angle / 360 * 3.14 * radius ** 2
#     print(f"此扇形面积为：{sector_area}")
#     return sector_area
#
# calculate_sector1 =  calculate_sector(160 , 30 )
#
# calculate_sector2 = calculate_sector(60, 70 )
#



# # 实践时间
# def calculate_BMI(height,weight):
#     BMI = weight/(height ** 2)
#     if BMI <= 18.5:
#         print("您的BMI分类为：" + "偏瘦")
#     elif BMI >18.5 and BMI <= 25:
#         print("您的BMI分类为：" + "正常")
#     elif BMI > 25 and BMI <= 30:
#         print("您的BMI分类为：" + "偏胖")
#     else:
#         print("您的BMI分类为：" + "肥胖")
#     return BMI
#
# calculate_BMI1 = calculate_BMI(1.65, 52)

# 参考答案：

# 实践时间--定义函数
def calculate_BMI(height,weight):
    BMI = weight/(height ** 2)
    if BMI <= 18.5:
        category = "偏瘦"
    elif BMI >18.5 and BMI <= 25:
        category = "正常"
    elif BMI > 25 and BMI <= 30:
        category = "偏胖"
    else:
        category = "肥胖"
    print("您的BMI分类为：" + category)
    return BMI

calculate_BMI1 = calculate_BMI(1.65, 52)

