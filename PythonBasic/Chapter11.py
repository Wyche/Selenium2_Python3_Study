####################文件和流####################

####################打开文件####################
#open函数，open(name[, mode[, buffering]])
#返回一个文件对象
#f = open(r'C:\Users\wanyiche\Desktop\Python\somefile.txt')

#文件模式
#'r' 读模式
#'w' 写模式
#'a' 追加模式
#'b' 二进制模式
#'+' 读/写模式，需要配合r/w/a一起使用

#缓冲
#第三个参数控制文件的缓冲
#0/False，I/O无缓冲
#1/True，I/O有缓冲，使用flush或者close才会更新硬盘上的数据
#大于1的数字代表缓冲区的大小（单位是字节）
####################打开文件####################

####################基本文件方法####################
#三种标准的流
#sys.stdin，数据输入的标准源
#sys.stdout，数据输出的标准源
#sys.stderr，错误信息

#读和写
f = open(r'somefile.txt', 'w')
f.write('Hello, ')
f.write("World!")
f.close()

f = open(r"somefile.txt", 'r')
#告诉流要读多少个字符（字节）
print(f.read(4)) #Hell
print(f.read()) #o, World!

#管式输出
#使用管道可以在一个命令之后续写其他的多个命令，管道符号（|）将一个命令的标准输出和下一个命令的标准输入连在一起
#Unix的shell

#随机访问
#文件中随意移动读取位置也是可以的，使用类文件对象的方法seek和tell来直接访问感兴趣的部分
#seek(offset[, whence])，把当前位置移动到由offest和whence定义的位置
#offset类是一个字节数，表示偏移量
#whence默认是0，表示偏移量是从文件开头计算的；1，相对于当前位置的移动；2，相对于文件结尾的移动
f = open(r'C:\Users\wanyiche\Desktop\Python\somefile2.txt', 'w')
f.write('01234567890123456789')
f.seek(5)
f.write('Hello, World!')
f.close()
f = open(r'C:\Users\wanyiche\Desktop\Python\somefile2.txt')
print(f.read())
#tell方法返回当前文件的位置如下
print(f.tell())

#读写行
#file.readline读取单独的一行（从当前的位置开始直到一个换行符出现，也读取这个换行符）
#readlines可以读取一个文件中的所有行并将其作为列表返回
#writelines与readlines相反，传给它一个字符串的列表（任何序列或者可迭代的对象），把所有的字符串写入文件（或流）
f = open(r"C:\Users\wanyiche\Desktop\Python\somefile3.txt", 'r+')
file = f.readlines()
for i in range(0, len(file)):
    print(file[i])
file2 = ['handsome\n', 'wyche\n', 'happy', 'birthday']
f.writelines(file2)
f.close()

#关闭文件
#使用close()方法关闭文件，为了确保文件被关闭，应该使用try/finally语句，在finally子句中调用close方法
#为了这种情况设计了with语句
#with open("somefile.txt") as somefile:
#    do_something(somefile)
#文件在语句结束后会被自动关闭，即使由于异常引起的结束也是如此
#Python2.5版本之后，with语句可以直接使用

#数据可能被缓存了，直到关闭文件才会被写入到文件，需要调用文件对象的flush方法
#with语句实际是很通用的结构，允许使用所谓的上下文管理器，一种支持__enter__和__exit__两个方法的对象
#__enter__方法不带参数，进入with语句块的时候被调用，放回值绑定到as关键字之后的变量
#__exit__方法带有3个参数，异常类型、异常对象和异常回溯，离开方法时被调用；如果__exit__返回false，所有异常都不会处理

#对文件内容进行迭代
def process(string):
    print("Processing: ", string)

#每个字符循环
f = open("somefile.txt")
char = f.read(1)
while char:
    process(char)
    char = f.read(1)
f.close()

f = open("somefile.txt")
while True:
    char = f.read(1)
    if not char: break
    process(char)
f.close()

#按行操作
#处理文本文件时，对文件进行迭代而不是处理单个字符，处理行和处理字符一样，使用readline方法
f = open("somefile3.txt")
while True:
    line = f.readline()
    if not line: break
    process(line)
f.close()

f = open("somefile.txt")
for char in f.read():
    process(char)
f.close()

f = open("somefile3.txt")
for line in f.readlines():
    process(line)
f.close()

#使用fileinput实现懒惰行迭代
#对一个非常大的文件进行迭代时，readlines会占用太多的内存
import fileinput
for line in fileinput.input("somefile3.txt"):
    process(line)

#文件迭代器
#Python2.2开始文件对象是可迭代的，可以直接在for循环中使用它们
f = open("somefile3.txt")
for line in f:
    process(line)
f.close()
#sys.stdin是可迭代的，就像其他文件对象
    
####################基本文件方法####################
