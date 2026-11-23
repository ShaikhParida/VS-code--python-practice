house_work_count = int(input("请输入本月的家务次数"))
red_envelope = int(input("请输入本月的红包个数"))
shopping_count = int(input("请输入本月的陪逛街次数"))
has_been_angry = bool(int(input("请输入本月是否有惹女朋友生气行为"))) # 0表示无/1表示有

# if house_work_count > 10:
#     if red_envelope > 1:
#         if shopping_count > 1:
#             if has_been_angry == False:
#                 print("摩拳擦掌等待Switch")
#             else:
#                 print("Switch随风散去。。。")
#         else:
#             print("Switch随风散去。。。")
#     else:
#         print("Switch随风散去。。。")
# else:
#     print("Switch随风散去。。。")

if(house_work_count > 10 and red_envelope > 1 and shopping_count > 1 and has_been_angry == False):
    print("摩拳擦掌等待Switch")
else:
    print("Switch随风散去。。。")