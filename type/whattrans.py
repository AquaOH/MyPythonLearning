# 本文件介绍转义符系列

# 首先介绍换行符
# 1.换行符\n,使用时会令文本换行
print('---分割线---')
print('\n', end='')
print('---分割线---')
# 特别的，如果\n后接了一个数字类
t = 114514
m = 1919810
print('\n', t, m)  # 会莫名多一格空格在第一个数字开头
print(t, m)  # 单独使用时无此类问题

print("---分割线---")

# 2.回车符\r
# 方言：作为单独字符使用时,将回车符号后面相邻内容放到开头，并添加一个空格(pycharm)
# 添加空格测试
print(t, '\r')
print(t)
print('\r', t)
print("---分割线---")
# 放到开头与添加空格测试
str1 = "aquaoh.love"
str2 = "test"
str3 = "liitle"
print(str1, '\r', str2, str3)
print(str2, '\r', str1, str3)

print('---分割线---')
# 方言2：在字符串中使用时,将回车符后所有内容放到开头，并覆盖原来字符(仅vscode)
# 会一直覆盖到后面内容用完
# 在pycharm中会直接只输出\r后面内容，且不添加空格
print("abcdefghijk\r123456")
print("abcde\r123456789")
print('abcde\r123456\rzxcvbnm')  # 连用也是这样,pycharm里则直接看最后的\r后面内容即可

print('---分割线---')


# 3.水平制表符/t
# 水平制表符，也即 Tab 键，一般相当于四个空格。
# eg = none


# 4.蜂鸣器响铃\a
# 时代眼泪


# 5.退格\b
# 将光标移动至前一位置,并丢弃之前位置内容,若有新内容，则接着光标写(pycharm)
print('123456\b')
print('123456\ba')
print('123456\b\ba')

# 6.反斜杠输出\\
print('---分割线---')
print('\\')

# 7.单引号输出\'
print('---分割线---')
print('\'')

# 8.双引号输出\"
print('---分割线---')
print("\"")

# 9.字符串行尾续行符
# 表示字符串未写完，转到下一行继续写
print('这是第一部分\
这是第二部分\
这是第三部分\
这是第四部分')

# 10.转义数字匹配码表
# 以/开头表示后跟八进制形式的编码值
# 以/x开头表示后跟16进制形式的编码值
'''
a在10进制中ansii编码值为
'''