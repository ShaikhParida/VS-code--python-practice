# 任务1：在一个新的名为"poem.txt"的文件里，写入以下内容：
# 我欲乘风归去，
# 又恐琼楼玉宇，
# 高处不胜寒。
with open("./poem.txt","w",encoding="utf-8") as f:
    f.write("我欲乘风归去，\n")
    f.write("又恐琼楼玉宇，\n")
    f.write("高处不胜寒。\n")

with open("./poem.txt","r",encoding="utf-8") as f:
    content = f.read()
    print(content)


# 任务2：在上面的"poem.txt"文件结尾处，添加以下两句：
# 起舞弄清影，
# 何似在人间。
with open("./poem.txt","a",encoding="utf-8") as f:
    f.write("起舞弄清影，\n")
    f.write("何似在人间。")

with open("./poem.txt","r",encoding="utf-8") as f:
    content = f.read()
    print(content)


