####################异常####################
#Python用异常对象（exception object）来表示异常情况
#按自己的方式出错，引发异常，创建自己的异常类型

#raise语句
#raise Exception

#捕捉异常
#使用try/except语句来实现,try抛出异常，except捕捉异常并处理
#想想如何利用这一特性进行自动化测试
try:
    x = int(input("number:"))
    y = int(input("number:"))
    print(x/y)
except ZeroDivisionError:
    print("the second number can't be zero!")
#可以设置多个except语句来捕捉不同类型的错误，进行不同的处理；也可以用一个except语句捕捉多个类型异常，以元组形式将其列出
except (ZeroDivisionError, TypeError, NameError):
    print("Your numbers were bogus...")

#捕捉对象，在except子句中访问异常对象本身
try:
    x = int(input("number:"))
    y = int(input("number:"))
    print(x/y)
except (ZeroDivisionError, TypeError, NameError) as e:
    print(e)

#全捕捉
try:
    x = int(input("number:"))
    y = int(input("number:"))
    print(x/y)
except:
    print("Something wrong happened...")
#这样的异常捕捉往往是危险的，也可以使用except Exception as e

#循环除法，正确后退出
while True:
    try:
        x = int(input("number:"))
        y = int(input("number:"))
        print(x/y)
    except Exception as e:
        print("Invalid input:", e)
        print("Please try again")
    else:
        break

#finally子句，用来在可能的异常后进行清理
#注意：用于关闭文件或者网络套接字时会非常有用，Python2.5之后，可以自由组合这些子句

#异常和函数
#如果异常在函数内引发而不被处理，就会传播至函数调用的地方；然后还没被处理，就会继续传播，直到到达主程序，最后程序带着栈跟踪中止

#应该习惯使用try/except语句，而非if/else语句来针对程序的异常
#Leap Before You Look
