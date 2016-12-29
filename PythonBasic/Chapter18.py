####################程序打包####################

#Distutils，是每个程序员工具包内的基础工具
#相关内容可以参考Python参考库中的：Distributing Python Modules 和 Installing Python Modules

#示例1
'''
from distutils.core import setup

setup(name='Hello',
      version='1.0',
      description='A simple example',
      author='Wyche Wang',
      py_modules=['hello'])
'''
