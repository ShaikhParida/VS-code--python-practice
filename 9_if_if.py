# mood_index是0到100之间的整数
# is_at_home为布尔值
mood_index = int(input("对象今天的心情指数是："))
is_at_home = bool(int(input("对象是否在家：")))

if mood_index < 60:
    if is_at_home:
        print("放弃游戏，低调做人")
    else:
        print("自由！")
else:
    print("爽飞了！")
