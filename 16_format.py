# # 土方法
#
# contacts = ["老余","老林","老陈","老曾","老李","老张"]
#
# for name in contacts:
#     message_content = name + "：岁始之乐，点翠画柳喜开颜。\
#     云雾散开，良辰美景共团圆。祝福" + name + \
#     "及家人新年快乐，平安顺遂，虎年大吉！"
#
# send_message(name, message_content)
#



# # format方法1
# year = "虎"
# name = "老林"
#
# message_content = """
# 律回春渐，新元肇起。
# 新岁甫至，福气东来。
# 金{0}贺岁，欢乐祥瑞。
# 金{0}敲门，五福临门。
# 给{1}及家人拜年了！
# 新春快乐，{0}年大吉！
# """.format(year, name)
#
# print(message_content)



# # format方法2
# year = "虎"
# name = "老林"
#
# message_content = """
# 律回春渐，新元肇起。
# 新岁甫至，福气东来。
# 金{current_year}贺岁，欢乐祥瑞。
# 金{current_year}敲门，五福临门。
# 给{receiver_name}及家人拜年了！
# 新春快乐，{current_year}年大吉！
# """.format(receiver_name = name,
#            current_year = year)  #等号前后分别是关键字、参数值
#
# print(message_content)



# # f-字符串方法
# year = "虎"
# name = "老林"
#
# message_content = f"""
# 律回春渐，新元肇起。
# 新岁甫至，福气东来。
# 金{year}贺岁，欢乐祥瑞。
# 金{year}敲门，五福临门。
# 给{name}及家人拜年了！
# 新春快乐，{year}年大吉！
# """
#
# print(message_content)

gpa_dict = {"小明":3.251, "小花":3.869, "小李":2.683,
            "小张":3.685}

for name,gpa in gpa_dict.items():
    print("{0}你好，你当前的绩点为：{1}".format(name,gpa))
#format形式不用转化为浮点数