####################序列通用操作####################
#Indexing
greeting = "Hello"
print(greeting[0]) #第一个元素
print(greeting[-1]) #右起第一个元素
print("Hello"[1]) #序列字面量直接使用索引，不需要借助变量引用
#print(input("Year: ")[3]) #直接对函数返回值进行索引操作

#Slicing
tag = "<a href='http://www.python.org'>Python web site</a>"
print(tag[9:30])
print(tag[32:-4])
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[3:6]) #[4,5,6]
print(numbers[-3:]) #如果分片所得部分包括序列结尾的元素，冒号后的索引置空即可
print(numbers[:3]) #规则同样适用于序列开始的元素
#提取域名
#url = input("Please enter the URL: ")
#domain = url[11:-4]
#print("Domain name: " + domain)
print(numbers[0:10:2]) #步长为2，输出[1,3,5,7,9]
print(numbers[10:0:-2]) #步长为-2，从右边往左提取元素，输出[10,8,6,4,2]

#Adding
print([1,2,3] + [4,5]) #[1, 2, 3, 4, 5]
print("hello" + "world") #helloworld

#Multiplying
print("python " * 5) #python python python python python
print([1,2] * 5) #[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
sequence = [None] * 10 #初始化一个长度为10的列表

#成员资格
permissions = "rw"
print('w' in permissions) #True
print('x' in permissions) #False
users = ['mlh', 'foo', 'bar']
#print(input('Enter your name: ') in users)

#长度、最小值、最大值
numbers = [100,34,678]
print(len(numbers))
print(min(numbers))
print(max(numbers))
####################序列通用操作####################



####################列表####################
#list函数
print(list("Hello")) #['H', 'e', 'l', 'l', 'o']
print(list((1,2,3))) #[1, 2, 3]

#元素赋值
x=[1,1,1]
x[1] = 2
print(x)

#删除元素
names = ["A","B","C","D"]
del names[2]
print(names) #['A', 'B', 'D']

#分片赋值
name = list("Perl")
print(name) #['P', 'e', 'r', 'l']
name[2:] = list("ar")
print(name) #['P', 'e', 'a', 'r']
name[1:] = list("ython")
print(name) #['P', 'y', 't', 'h', 'o', 'n']
numbers = [1,5]
numbers[1:1] = [2,3,4]
print(numbers) #[1, 2, 3, 4, 5]
numbers[1:4] = []
print(numbers) #[1, 5]

#append方法
lst = [1,2,3]
lst.append(4)
print(lst) #[1, 2, 3, 4]

#count方法
x = [[1,2],1,1,[2,1,[1,2]]]
print(x.count(1)) #2，两个独自出现的1才是要计算的元素

#extend方法
a = [1,2]
b = [3,4]
a.extend(b)
print(a) #[1, 2, 3, 4]
#注意与连接操作的不同
a = [1,2]
b = [3,4]
print(a+b) #[1, 2, 3, 4]
print(a) #[1, 2]，列表a没有被改变
#分片赋值实现extend方法
a = [1,2]
b = [3,4]
a[len(a):] = b
print(a) #[1, 2, 3, 4]

#index方法
knights = ["We", "are", "the", "who", "say"]
print(repr(knights[3])) #'who'
print(knights.index('who')) #3
#print(knights.index("i")) #抛出异常

#insert方法
numbers = [1,2,3,5]
numbers.insert(3,"four")
print(numbers) #[1, 2, 3, 'four', 5]

#pop方法
x = [1,2,3]
print(x.pop()) #3
print(x) #[1, 2]
print(x.pop(0)) #指定抛出索引对应的元素，1
print(x) #[2]
#出栈入栈相互抵消
x = [1,2,3]
x.append(x.pop())
print(x) #[1, 2, 3]

#remove方法
x = ["to","be","or","not","to","be"]
x.remove("be")
print(x) #['to', 'or', 'not', 'to', 'be']
#x.remove("bee") #抛出异常

#reverse方法
x = [1,2,3]
x.reverse()
print(x) #[3, 2, 1]

#sort方法
x = [4,6,2,1,7,9]
x.sort()
print(x) #[1, 2, 4, 6, 7, 9]
#sorted函数
x = [4,6,2,1,7,9]
y = sorted(x)
print(x) #[4, 6, 2, 1, 7, 9]
print(y) #[1, 2, 4, 6, 7, 9]

#高级排序
x = ["asadf","sc","dfsa","etqerq"]
x.sort(key=len)
print(x) #['sc', 'dfsa', 'asadf', 'etqerq']
x.sort(key=len,reverse=True)
print(x) #['etqerq', 'asadf', 'dfsa', 'sc']
####################列表####################



####################元组####################
#tuple函数
print(tuple([1,2,3])) #(1, 2, 3)
print(tuple("abc")) #('a', 'b', 'c')

#创建元组
x = 1,2,3
print(x)

#元组分片
print(x[0:2])
####################元组####################


