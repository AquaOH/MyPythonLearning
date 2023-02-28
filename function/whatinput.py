# 介绍input函数用法
"""
函数用法: str = input(tipmsg)  #其中tipmsg为字符串，input输出内容也为字符串,需要变量承接
"""
a = input("输入一个整数")
b = input("输入另一个整数")
print("aType: ", type(a))
print("bType: ", type(b))  # 仍然为string类型
result = a + b  # 只是相当于字符串拼接而非整数相加
print("resultValue: ", result)
print("resultType: ", type(result))  # 还是string类型

# python有非常便利的转换数据类型
c = input("输入一个整数")
d = input("输入一个浮点数")
e = int(c)
f = float(d)
print("eType: ", type(e))
print("fType: ", type(f))  # 已转换类型
result = e + f
print("resultValue: ", result)
print("resultType: ", type(result))  # 已成功变为float类型
