####################魔法方法、属性和迭代器####################
#Python中，有的名称前后会加上两个下划线，这种拼写表示名字有特殊含义
#这些名字组成的集合所包含的方法称为魔法方法，如果对象实现了这些方法，那么这个方法会在特殊的情况下被调用

#新式类必要语句
__metaclass__ = type
#可以在自己的类的作用域中对__metaclass__变量赋值，这样只会为这个类设定元类
#元类是其他类（或类型）的类，上网搜索术语python metaclasses

#在Python3.0中没有“旧式”的类，不需要显式地子类化object或者将元类设置为type

#构造方法
#当一个对象被创建后，会立即调用构造方法
class FooBar:
    def __init__(self):
        self.somevar = 42

f = FooBar()
print(f.somevar)

#带有参数的构造方法
class FooBar_2:
    def __init__(self, value=42):
        self.somevar = value

f2 = FooBar_2("hello")
print(f2.somevar)

#析构方法，__del__，在对象要被垃圾回收之前调用；调用时间不可知，尽量避免使用

#重写一般方法和特殊的构造方法
#子类中增加功能的最基本方式就是增加方法
class A:
    def hello(self):
        print("A")
class B(A):
    def hello(self):
        print("B")

a = A()
b = B()
a.hello()
b.hello()
#重写是继承机制中的一个重要内容，对于构造方法尤其重要
#如果一个类的构造方法被重写，就需要调用超类的构造方法，否则对象可能不会被正确的初始化，有两种方法可以达到这个目的
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("Aaaah...")
            self.hungry = False
        else:
            print("No, thanks!")

class SongBird(Bird):
    def __init__(self):
        #方法一：调用未绑定的超类构造方法（很多遗留的代码会用到这个方法）
        #调用一个实例的方法时，该方法的self参数自动绑定到实例上（绑定方法）
        Bird.__init__(self) #直接调用类的方法（比如Bird.__init__），就没有实例会被绑定，就可以自由地提供需要的self参数，这就是未绑定方法
        #方法二：调用super函数，只能在新式类中使用，当前的类和
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)

b = Bird()
b.eat()
b.eat()

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()

class Bird2:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("Aaaah...")
            self.hungry = False
        else:
            print("No, thanks!")

class SongBird2(Bird):
    def __init__(self):
        #方法二：调用super函数，只能在新式类中使用，当前的类和对象可以作为super函数的参数使用，返回的对象的任何方法都是调用超类的方法
        super(SongBird2, slef).__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)

b = Bird()
b.eat()
b.eat()

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()
#大多数情况下，调用超类的未绑定的构造方法（或者其他方法）是更好的选择

#成员访问
#基本的序列和映射规则
#序列和映射是对象的集合，为了实现它们基本的行为（规则），如果对象是不可变的，需要使用两个魔法方法；如果对象是可变的需要使用4个
#__len__(slef)，返回集合中所含项目的数量
#__getitem__(self, key)，返回与所给键对应的值
#__setitem__(self, key, value)，按一定的方式存储和key相关的value
#__delitem__(self, key)，对一部分对象使用del语句时被调用，同时必须删除和元素相关的键
#更多的魔法方法可以参考帮助手册

#属性
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height

r = Rectangle()
r.width = 10
r.height = 5
print(r.getSize())
r.setSize((150,100))
print(r.width)

#property函数
class Rectangle2:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize, setSize)

print("......Rectangle2......")
r2 = Rectangle2()
r2.width = 10
r2.height = 5
print(r2.size)
r2.size = 250, 200
print(r2.width)
#property的四个参数分别为fget、fset、fdel和doc；新式类中应该使用property函数而不是访问器方法

#静态方法和类成员方法
#静态方法和类成员方法分别在创建时被装入Staticmethod类型和Classmethod类型的对象中
class MyClass:
    #静态方法的定义没有self参数，且能够被类本身直接调用
    def smeth():
        print("This is a static method")
    smeth = staticmethod(smeth)

    #类方法在定义时需要名为cls的类似于slef的参数，可以用类的具体对象调用，cls参数是自动被绑定到类的
    def cmeth(cls):
        print("This is a class method of", cls)
    cmeth = classmethod(cmeth)

#装饰器
class MyClass2:
    @staticmethod
    def smeth():
        print("static method")

    @classmethod
    def cmeth(cls):
        print("class method")

MyClass2.smeth()
MyClass2.cmeth()
#注：静态方法和类成员方法在Python中不是很重要，但是不能忽视其应用

#迭代器
#__iter__迭代器规则的基础，只要对象实现了__iter__方法就可以对其进行迭代
#__iter__方法返回一个迭代器，所谓的迭代器就是具有next方法（调用时不需要任何参数）的对象，调用next方法时，迭代器会返回它的下一个值
#Python3.0的新规则中，迭代器对象应该实现__next__方法，而不是next；而新的内建函数next可以用于访问这个方法，next(it)等同于3.0之前版本中的it.next()
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        return self.a
    def __iter__(self):
        return self
#一个实现了__iter__方法的对象是可迭代的；一个实现了__next__方法的对象则是迭代器
fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break
#内建函数iter可以从可迭代的对象中获得迭代器
it = iter([1,2,3])
print(next(it))
#从迭代器得到序列
class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value
    def __iter__(self):
        return self

ti  = TestIterator()
print(list(ti))

#生成器
#Python新引入的概念，也叫简单生成器；生成器可以帮忙写出非常优雅的代码，不使用也是可以的
#生成器是一种用普通的函数语法定义的迭代器
nested = [[1,2],[3,4],[5]]
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

for num in flatten(nested):
    print(num)
#任何包含yield语句的函数称为生成器，每次产生多个值；每次产生一个值（使用yield语句），函数就会被冻结

#递归生成器
def flatten2(nested):
    try:
        for sublist in nested:
            for element in flatten2(sublist):
                yield element
    except TypeError:
        yield nested

#添加检查语句的生成器
def flatten3(nested):
    try:
        #不要迭代类似字符串的对象,将传入的对象和一个字符串拼接，是最简单、快速的方法方法
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten3(sublist):
                yield element
    except TypeError:
        yield nested

#通用生成器
#生成器由两个部分组成：生成器的函数和生成器的迭代器
#生成器的函数是用def语句定义的，包含yield的部分；生成器的迭代器是这个函数返回的部分
#生成器方法
def repeater(value):
    while True:
        new = (yield value)
        if new is not None: value = new

r = repeater(42)
print(next(r))
print(r.send("Hello, world!"))
#throw方法、close方法

#模拟生成器
#生成器在旧版本的Python中是不可用的，使用普通函数模拟生成器
#result = []放在函数体的开始处
#使用result.append(some_expression)替换yield some_expression
#函数末尾添加return result
def flatten4(nested):
    result = []
    try:
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten4(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result

    




