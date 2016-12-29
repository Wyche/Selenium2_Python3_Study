####################字符串####################
#字符串格式化
format = "Hello, %s. Welcome to %s world"
values = ("Wyche", "Python's")
print(format % values) #Hello, Wyche. Welcome to Python's world

#find方法
title = "Monty Python's Flying Circus"
print(title.find('Monty')) #0
print(title.find("Python")) #6
#指定查找范围
a = "abcdefgabcdefgabc"
print(a.find("ab",7,-1)) #7
print(a.find("ab",8,-2)) #-1

#join方法
seq = ["1", "2", "3"]
print("+".join(seq)) #1+2+3，使用+来连接seq列表中的各个元素
seq = ("a", "b", "c")
print("+".join(seq)) #a+b+c，使用+来连接seq元组中的各个元素

#split方法
#join方法的逆方法
print("1+2+3+4".split('+')) #['1', '2', '3', '4']
print("C:/bin/123/wo".split('/')) #['C:', 'bin', '123', 'wo']
print("My name is wyche".split(" ")) #['My', 'name', 'is', 'wyche']

#lower方法
#小写输出字符串
print("HELLO".lower()) #hello
#upper方法
#大写输出字符串
print('hello'.upper()) #HELLO

#strip方法
#返回去除两侧空格的字符串，与lower()一起使用可以方便的比对输入和存储的值
print("    hello   world   ".strip()) #hello   world
#指定需要去除的字符
print("*** SPAM * for * everyone!!! ***".strip(' *!')) #SPAM * for * everyone

#replace方法
print("Hello, this is wyche. Who is that?".replace("is", "IS")) #Hello, thIS IS wyche. Who IS that?

#translate方法
#与replace类似，但是只处理单个字符
#from string import maketrans
#table = maketrans('cs', 'kz')
#print('this is an incredible test'.translate(table, ' '))
####################字符串####################

