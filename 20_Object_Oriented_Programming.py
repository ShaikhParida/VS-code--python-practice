# class NameOfClass:
#     # 接下来是一些定义类的代码
#     # ...

# 变量名-下划线命名法-用下划线分分隔单词
# 类名-Pascal命名法-每个单词仅首字母大写分隔单词

# # 普通命名-不灵活
# class CuteCat:
#     def __init__(self):
#         self.name = "Lambton"
#
# cat1 = CuteCat()
# print(cat1.name)


# 另一种命名
class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color
cat1 = CuteCat("Jojo",2,"橙色")
print(f"小猫{cat1.name}的年龄是{cat1.age},花色是{cat1.color}")







