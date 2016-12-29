####################抽象####################

#创建函数
#使用def语句
def hello(name):
    return 'Hello, '+ name + "!"
print(hello("wyche"))

def fibs(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result
print(fibs(10))

#文档化函数
def square(x):
    'Calculates the square of the number x'
    return x*x

#并非真正函数的函数
#其实返回了None，有些语言中称为过程，Python中只有函数
def test():
    print("This is printed")
    return
    print("This is not")

####################参数####################
#def语句中函数名后的通常叫形参，调用函数时提供的是实参
def try_to_change(name):
    name = 'Mr. Gumby'
#函数内部参数赋予新值不会改变外部任何变量的值

#当两个变量同时引用一个列表的时候，任何修改都会改变列表的值
#为了避免这种情况，可以复制一个列表的副本，使用切片操作
names = ['Mrs. Entity', 'Mrs. Thing']
n = names[:]
print(n is names)

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

#Python中函数只能修改参数对象本身，不能影响函数外的变量。
#迂回的办法，要么使用返回值，要么将值放在列表中
def inc(x): return x+1
foo = 10
foo = inc(foo)
print(foo)

def inc2(x):
    x[0] = x[0] + 1
foo = [10]
inc2(foo)
print(foo)

#关键字参数和默认值
#之前使用的参数叫做位置参数
def hello(name='Wyche', greeting='Hello'):
    print(greeting + ',' + name)
#如果不带参数调用函数，会使用默认值

#收集参数
def print_params(*params):
    print(params)
print_params(1,2,3)

def print_params_2(title, *params):
    print(title)
    print(params)
print_params_2('Params:', 1,2,3)
#*表示收集其余的位置参数，返回的是元组
#**能处理关键字参数，返回字典
def print_params_3(**params):
    print(params)
print_params_3(x=1, y=2, z=3)

def print_params_4(x, y, z=3, *pospar, **keypar):
    print(x,y,z)
    print(pospar)
    print(keypar)
print_params_4(1,2,3,5,6,7,foo=1,bar=2)

#参数收集逆过程
#还是使用*和**操作，在调用时使用，而非定义时
def add(x,y): return x+y
params = (1,2)
print(add(*params))

params = {'name': 'Sir Robin', 'greeting': 'Well met'}
hello(**params)
#注：*或者**只在定义函数（允许使用不定数目的参数）或者调用（“分隔”字典或者序列）时才有用，不要两边同时使用，没有意义。
####################参数####################

####################作用域####################
#可以把变量看作是值的名字，变量和所对应的值用的是“不可见”的字典。这就叫做命名空间或者作用域
#除了全局作用域，每个函数调用会创建一个新的作用域
#一般来说，读取全局变量并不是问题，但是如果全局变量名和局部变量名相同，全局变量会被屏蔽。此时可以使用globals()['parameter']函数
g_value = 2
def read_global():
    g_value = 1
    print(g_value+globals()['g_value'])
read_global() #3

#函数内部将值赋予一个变量，会自动变成局部变量，使用global声明，使其成为全局变量
#慎用！！
x = 1
def change_global():
    global x
    x += 1
change_global()
print(x) #2
####################作用域####################

####################递归####################
#函数调用函数称为嵌套；函数调用自身称为递归
#阶乘,普通版
def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result
#递归版
def factorial_2(n):
    if n == 1:
        return 1
    else:
        return n * factorial_2(n-1)
a = factorial_2(5)
print(a)

#幂，递归
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
b = power(2, 3)
print(b)

#二分查找
def search(sequence, number, lower, upper):
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle+1, upper)
        else:
            return search(sequence, number, lower, middle)

####################递归####################




