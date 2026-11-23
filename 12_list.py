# item1 = "键帽"
# item2 = "键盘"
shoppinglist_list = ["键盘","键帽"]
print(shoppinglist_list)
print("\n")

shoppinglist_list.append("显示器")   #对象.方法论（...）
print(len(shoppinglist_list))       #函数名(对象)
print(shoppinglist_list)
print("\n")

shoppinglist_list.remove("键帽")
print(len(shoppinglist_list))       #函数名(对象)
print(shoppinglist_list)
print("\n")

shoppinglist_list.append("硬盘")   #对象.方法论（...）
print(len(shoppinglist_list))       #函数名(对象)
print(shoppinglist_list)
print("\n")

shoppinglist_list[2] = "耳机"   #对象.方法论（...）
print(len(shoppinglist_list))       #函数名(对象)
print(shoppinglist_list)
print("\n")




print("\n")
print("\n")
print("\n")

# 可变： 列表list
# 不可变： 字符串str、整数int、浮点型float、布尔类型bool
# 例如
# s = "Hello"
# print(s.upper())
# print(s)
# 屏幕会显示：
# HEllO
# Hello

list1 = ["Hello"]
list1.append(66.6)
list1.append(True)
list1.append(False)
print(list1)

print("\n")
print("\n")


num_list = [1,13,7,2,96]
print(max(num_list))
print(min(num_list))
print(sorted(num_list))

print("\n")
print("\n")

price = [799,1024,200,800]
print(max(price))
print(min(price))
print(price)
sorted_price = sorted(price)
print(sorted_price)


