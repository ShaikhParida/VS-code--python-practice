def calculate_and_print(num,calculator,formatter):
    result = calculator(num)
    formatter(num,result)

def print_with_vertical_bar(num,result):
    print(f"""
    | 数字参数 |{num}|
    | 计算结果 |{result}|""")

def calculator_square(num):
        return num * num

def calculate_cube(num):
        return num * num * num

def calculator_plus_10(num):
        return num + 10


calculate_and_print(3, calculator_square,print_with_vertical_bar)      # 高阶函数

calculate_and_print(7, lambda num: num * 5,print_with_vertical_bar)    # 匿名函数


