# 什么时候用继承
# A是B   class A(B):
# 人类是动物 class Human(Animal):
# 新能源车是车 Class ElectricCar(Car)

# 类继承练习：人力系统
# - 员工分为两类：全职员工 FullTimeEmployee、兼职员工 PartTimeEmployee。
#   都具备"打印信息 print_info"（打印姓名、工号）方法。
# - 全职有"日薪 monthly_salary"属性，
#   兼职有"日薪 daily_salary"属性、"每月工作天数 work_days"的属性。
# - 全职和兼职都有"计算月薪 calculate_mouthly_pay"的方法，但具体计算过程不一样。

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"员工名字：{self.name},工号：{self.id}")

class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name,id)
        self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days


    def calculate_monthly_pay(self):
        return self.daily_salary * self.work_days

zhangsan = FullTimeEmployee("张三","1001","6000")
lisi = PartTimeEmployee("李四","1002",130,10)
zhangsan.print_info()
print(zhangsan.calculate_monthly_pay())

lisi.print_info()
print(lisi.calculate_monthly_pay())


# class Employee:
#     def __init__(self, name, number):
#         self.name = name
#         self.number = number
#
#     def print_info(self):
#         print("姓名：" + self.name)
#         print("工号：" + self.number)
#
#
# class FullTimeEmployee(Employee):
#     def __init__(self, name, number):
#         super().__init__(name,number,)
#         self.monthly_salary = 5000
#
#     def calculate_salary(self):
#

