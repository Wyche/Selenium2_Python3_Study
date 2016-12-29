####################条件、循环和其他语句####################

#序列解包
x, y, z = 1, 2, 3
print(x,y,z)
x, y = y, x
print(x,y,z)
values = 1,2,3
print(values) #(1, 2, 3)
x, y, z = values
print(x) #1
scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, value = scoundrel.popitem()
print(key) #name
print(value) #Robin
#Python3.0中的解包特性
a, b, *rest = [1,2,3,4]
print(rest) #[3, 4]

#链式赋值
x = y = 1
print(x,y) #1 1

#增量赋值
x = 2
x += 1
print(x) #3
fnord = 'foo'
fnord += 'bar'
fnord *= 2
print(fnord) #foobarfoobar

#条件和条件语句
num = int(input('Enter a number: '))
if num > 0:
    print('The number is positive.')
elif num < 0:
    print('The number is negative.')
else:
    print('The number is zero')

#同一性运算符 is
#判断是否为同一对象
x = y = [1,2,3]
z = [1,2,3]
print(x == y) #True
print(x == z) #True
print(x is y) #True
print(x is z) #False

#断言
#条件必须满足才能让程序正常工作
a = 1
assert 0 < a < 100

#循环
name = ''
while not name.strip(): #使用strip方法只是为了防止输入空格
    name = input("Enter your name: ")
print("Hello, %s!" % name)

for number in range(1, 11):
    print(number)

#并行迭代
names = ['anne','beth','george','damon']
ages = [12,45,32,102]
for name, age in zip(names, ages):
    print(name,'is',age,'years old.')

#按索引迭代
#enumerate函数可以实现

#翻转和排序迭
#不是原地修改对象
print(sorted([4,3,6,8,3]))
print(list(reversed("Hello, World!")))

#跳出循环
#break，跳出循环
#continue，结束当前迭代，进入下一次迭代

#列表推到式，轻量级循环
print([x*x for x in range(10)]) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print([x*x for x in range(10) if x%3 == 0])
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])

#del删除
#Python会进行垃圾收集，来删除不再被使用的值，del语句可以删除变量名
x = 1
print(x)
del x #执行结果：name 'x' is not defined
x = ["Hello", "World"]
y = x
del x
print(y) #x被删除了，但是列表并没有，y也没有

#exec, eval
#exec语句执行一个字符串。
#并不常用，最好在作用域中使用
scope = {}
exec('x = 2') in scope


