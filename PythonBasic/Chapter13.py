####################数据库####################
#使用数据库很简单，创建连接并且获得该连接的游标
#使用execute方法执行SQL查询
#用fetchall等方法提取结果
import sqlite3

conn = sqlite3.connect('food.db')
curs = conn.cursor()

curs.execute('''
CREATE TABLE food (
  id         TEXT         PRIMARY KEY,
  desc       TEXT,
  water      FLOAT,
  kcal       FLOAT
)
''')

query = ['INSERT INTO food VALUES("001","first",10,20)', 'INSERT INTO food VALUES("002","second",30,120)', 'INSERT INTO food VALUES("003","third",5,30)']
for q in query:
    curs.execute(q)

conn.commit()
conn.close()


conn = sqlite3.connect('food.db')
curs = conn.cursor()

query = 'SELECT * FROM food WHERE id = "002"'
print(query)
curs.execute(query)
print(curs.fetchall())

conn.close()
    

