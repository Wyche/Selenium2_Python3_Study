####################字典####################

#创建字典
phonebook = {"Alice": "2341", "Beth": "9102"}
#键-值对称为项

#dict函数，建立字典
items = [('name', 'Wyche'), ('age', 24)]
d = dict(items) 
print(d) #{'name': 'Wyche', 'age': 24}
d = dict(name='Wyche', age=25)
print(d) #{'age': 25, 'name': 'Wyche'}

#基本的字典操作
#很多方面与序列类似
print(len(d)) #2
print(d['name']) #Wyche
d['name'] = "Ziv"
print(d['name']) #Ziv
del d['age']
print(d) #{'name': 'Ziv'}
print('name' in d) #True
#键可以是任意不可变类型
#字典的成员资格查找的是键，列表的成员资格查找的是值
x = []
#x[42] = 'Foobar' #抛出异常
y = {}
y[42] = 'Foobar' #程序正常

#字典的格式化字符串
phonebook['Cecil'] = '3258'
print("Cecil's phone number is %(Cecil)s." % phonebook) #Cecil's phone number is 3258.
#模板系统中的使用
template = '''<html>
<head><title>%(title)s</title></head>
<body>
<1>%(title)s</h1>
<p>%(text)s</p>
</body>'''
data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
print(template % data)

####################字典方法####################
#字典方法不会被频繁使用

#clear方法
#清除字典中的所有项，原地操作，无返回值
d = {}
d['name'] = 'Wyche'
d['age'] = 24
print(d) #{'name': 'Wyche', 'age': 24}
d.clear()
print(d) #{}

#copy方法
#返回一个具有相同键-值对的新字典，浅复制，值本身是相同的，并非副本
x = {'username': 'admin', 'machine': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machine'].remove('bar')
print(x) #{'machine': ['foo', 'baz'], 'username': 'admin'}
print(y) #{'machine': ['foo', 'baz'], 'username': 'mlh'}
#利用copy模块的deepcopy来进行深复制
from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print(c) #{'names': ['Alfred', 'Bertrand', 'Clive']}
print(dc) #{'names': ['Alfred', 'Bertrand']}

#fromkeys方法
#使用给定的键简历新的字典，每个键对应一个默认的None
print({}.fromkeys(['name', 'age'])) #{'age': None, 'name': None}

#get方法
#更宽松的方式访问字典项
d = {}
#print(d['name']) #抛出异常，因为d中没有键为‘name’的值
print(d.get('name')) #None
#get方法带来的灵活性使得程序做出合理反应

#has_key方法
#功能相当于in函数，Python3.0中不包括这个函数

#items方法
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.items()) #[('spam', 0), ('url', 'http://www.python.org'), ('title', 'Python Web Site')]

#keys方法
print(d.keys()) #dict_keys(['url', 'spam', 'title'])

#pop方法
d = {'x': 1, 'y': 2}
d.pop('x')
print(d) #{'y': 2}

#popitem方法
#弹出字典中的随机的项
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.popitem())

#setdefault方法
d = {}
d.setdefault('name', 'N/A')
print(d) #{'name': 'N/A'}
d['name'] = 'Gumby'
print(d) #{'name': 'Gumby'}
d.setdefault('name', 'N/A')

#update方法
#利用一个字典项更新另一个字典
#没有的进行添加，已经有的就会进行覆盖
d = {
    'title': 'Python',
    'url': 'http://',
    'changed': 'Mar 14'
    }
x = {'title': 'hello'}
d.update(x)
print(d) #{'url': 'http://', 'changed': 'Mar 14', 'title': 'hello'}

#values和itervalues方法
#以列表形式返回字典中的值
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d.values()) #dict_values([1, 3, 2])

####################字典方法####################

