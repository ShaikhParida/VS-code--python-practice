# 定义一个学生类
# 要求
# 1. 属性包括学生姓名、学号、以及语数英三科的成绩
# 2. 能够设置学生某科的成绩
# 3. 能够打印出该学生的所有科目成绩

class Student:                                        # 定义类
    def __init__(self,name,student_id):               # 定义方法
        self.name=name
        self.student_id=student_id
        self.grades = {"语文":0,"数学":0,"英语":0}      # 使用字典定义 定义键值对 科目为键 分数为值

    def set_grade(self, course, grade):               # 定义方法
        if course in self.grades:
            self.grades[course] = grade               # 将grade赋值给键值对的值  科目为键 分数为值

    def print_grades(self):
        print(f"学生{self.name},(学号:{self.student_id})的成绩为：")
        for course in self.grades:
            print(f"{course}: {self.grades[course]}分")

chen = Student("小陈","100618")
zeng = Student("小曾","100622")

print(zeng.name)
zeng.set_grade("语文",98)

zeng.set_grade("数学",97)
zeng.set_grade("英语",90)
zeng.print_grades()
