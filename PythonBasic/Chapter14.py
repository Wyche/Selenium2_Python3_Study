####################网络编程####################
#John Goerzen的Foundations of Python Network Programming

#socket模块
#网络编程中的一个基本组件就是套接字（socket），基本上是两个端点的程序之间的“信息通道”
#Python中的大多数网络编程都隐藏了socket模块的基本细节，不直接和套接字交互
#套接字包括两个：服务器套接字和客户机套接字
#一个套接字就是socket模块中的socket类的一个实例，实例化需要3个参数
#第1个参数是地址族（默认socket.AF_INET）
#第2个参数是流（socket.SOCK_STREAM，默认值）或数据报（socket.SOCK_DGRAM）
#第3个参数是使用的协议（默认是0）
#对于一个普通的套接字，不需要提供任何参数

#服务器端套接字使用bind方法后，再调用listen方法去监听某个特定的地址
#客户端套接字使用connect方法连接到服务器，connect方法中使用的地址与服务器bind方法中的地址相同

#服务器端套接字开始监听后，就可以接受客户端的连接，这个步骤使用accept方法来完成
#这个方法会阻塞（等待）直到客户机连接，然后返回一个格式为(client, address)的元组，client是一个客户端套接字，address是之前解释的地址
#这种形式的服务器编程称为阻塞或者同步网络编程
#套接字有两个方法：send和recv，用于传输数据

#SocketServer模块是标准库中很多服务器框架的基础，所有服务器框架都为基础服务器增加了特定的功能
#SocketServer包含4个基本的类：
#针对TCP流式套接字的TCPServer
#针对UDP数据报套接字的TDPServer
#针对性不强的UnixStreamServer和UnixDatagramServer

#如果编写一个SocketServer框架的服务器，会将大部分代码放在一个请求处理程序（request handler）中
#每当服务器收到一个请求，就会实例化一个请求处理程序，并且它的各种处理方法（handler method）会在处理请求时被调用
#具体调用哪个方法取决于特定的服务器和使用的处理程序类（handler class）

#多个连接
#分叉（forking）、线程（threading）、异步I/O（asynchronous I/O）
#分叉是针对于进程的，比较耗费资源，享有独立的内存；线程是轻量级的进程或子进程，所有的线程都存在于相同的（真正的）进程中，共享内存
#资源消耗下降，共享内存必须确保变量不会冲突，如果不想被同步问题所困扰，分叉是一个很好的选择
#现代操作系统（除Windows，它不支持分叉），分叉实际是很快的
#避免线程和分叉的另一种方法是转换到Stackless Python，支持一种叫做微线程的类线程的并行形式，比真线程的伸缩性要好
#异步I/O基本机制是select模块的select函数

#带有select和poll的异步I/O
#asyncore/asynchat框架和Twisted框架采用的方法是：只处理在给定时间内真正要进行通信的客户端
#不需要一直监听，只要监听（或读取）一会儿，然后把它放到其他客户端的后面
#select和poll函数都来自select模块，poll的伸缩性更好，但是只能在UNIX系统中使用
#select函数需要3个序列作为它的必选参数，还有一个可选的以秒为单位的超时时间作为第4个参数；3个序列用于输入、输出以及异常情况
#select函数的返回值是3个序列（一个长度为3的元组），每个代表相应参数的一个活动子集



