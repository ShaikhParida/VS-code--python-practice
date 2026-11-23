class Mammal:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.num_eyes = 2
    def breath(self):
        print(self.name + "在呼吸...")
    def poop(self):
        print(self.name + "在拉屎...")

class Human(Mammal):
    def __init__(self,name,sex):
        super().__init__(name,sex)
        self.has_tail = False           # has tail 属性不同
    def read(self):
        print(self.name + "在阅读...")

class Cat(Mammal):
    def __init__(self, name, sex):
        super().__init__(name,sex)
        self.has_tail = True            # has tail 属性不同
    def scratch_sofa(self):
        print(self.name + "在那抓沙发...")

cat1 = Cat("Jojo","男")
print(cat1.name)
cat1.poop()

# class Mammal:
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex
#         self.num_eyes = 2
#
#     def breath(self):
#         print(self.name + "在呼吸...")
#
#     def poop(self):
#         print(self.name + "在拉屎")
#
# class Human(Mammal):
#     def read(self):
#         print(self.name + "在阅读...")
#
# class Cat(Mammal):
#     def scratch_sofa(self):
#         print(self.name + "在抓沙发")
#     def poop(self):
#         print(self.name + "在猫砂上拉屎...")       # 先看所属的类有没有该方法，没有的话再去父类寻找
#
# cat1 = Cat("Jojo", "公")
# cat1.poop()                                      # 优先执行Cat类下的方法
