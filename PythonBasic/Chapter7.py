####################更加抽象####################
#创建自己的类
__metaclass__ = type #确定使用新式类
#新式类的语法中，需要在模块或脚本开始的地方使用上述语句
class Person:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print("Hello, world! I'm %s" % self.name)
#self是对于对象自身的引用，没有它的话，成员方法就没法访问他们要对其特性进行操作的对象本身了
foo = Person()
bar = Person()
foo.setName('Luke')
bar.setName('Anak')
foo.greet()
bar.greet()

print(foo.name)

#特性、函数和方法
#self参数事实上正是方法和函数的区别
#绑定方法将第一个参数绑定到所属的实例上，无需显式提供该参数
#子类调用超类的方法，直接通过类调用，没有绑定自己的self参数到任何东西上，称为非绑定方法
#Python并不直接支持私有方式，使用小技巧可以达成，在名字前加上双下划线即可
class Secretive:
    def __inaccessible(self):
        print("Bet you can't see me")

    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()

s = Secretive()
#s.__inaccessible() #抛出异常
s.accessible()
#其实，类的内部定义中，所有以双下划线开始的名字都被编译成前面加上单下划线和类名的形式。
s._Secretive__inaccessible() #可以调用，但是不应该这么做
#Python并没有真正的私有化支持

#类的命名空间
#所有位于class语句中的代码块都在特殊的命名空间中执行——类命名空间（class namespace），这个命名空间可由类内所有成员访问
class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members += 1

m1 = MemberCounter()
m1.init()
print(MemberCounter.members)
m2 = MemberCounter()
m2.init()
print(MemberCounter.members)
print(m2.members) 
print(m1.members)
#注意不同
m1.members = "Two"
print(m2.members) #2
print(m1.members) #Two

#指定超类
class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter): #SPAMFilter是Filter的子类
    def init(self): #重写Filter超类中的init方法
        self.blocked = ['SPAM']

f = Filter()
f.init()
print(f.filter([1,2,3]))
s = SPAMFilter()
s.init()
print(s.filter(['SPAM', 'SPAM', 'eggs', 'SPAM', 'bacon']))

#检查继承
print(issubclass(SPAMFilter, Filter))

#查看已知类的基类
print(SPAMFilter.__bases__)

#注:子类的实例就是父类的实例，想要知道对象属于哪个类，可以使用__class__特性
print(s.__class__)

#多个超类
#多重继承，除非特别熟悉，否则应该尽量避免使用
#当一个方法从多个超类继承，先继承的类中的方法会重写后继承的类中的方法。
#如果超类们共享一个超类，查找给定方法或者属性时访问超类的顺序称为MRO（Method Resolution Order）
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)

class Talker:
    def talk(self):
        print("Hi, my value is", self.value)

class TalkingCalculator(Calculator, Talker):
    pass

tc = TalkingCalculator()
tc.calculate("1+2*3")
tc.talk()

#接口和内省
#处理多态对象时，只要关心公开的方法和特性。Python中，不必显式地指定对象必须包含哪些方法才能作为参数接收。


