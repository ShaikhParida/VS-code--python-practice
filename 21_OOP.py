# 定义类和对应方法
class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color

    def speak(self):
        print("喵" * self.age)

    def think(self,content):
        print(f"小猫{self.name}在思考{content}")

# 定义对象
cat1 = CuteCat("Jojo",3,"橙色")

# 调用方法
print(f"小猫{cat1.name}的年龄是{cat1.age},花色是{cat1.color}")

cat1.think("现在去抓沙发还是去撕纸箱")
cat1.speak()


