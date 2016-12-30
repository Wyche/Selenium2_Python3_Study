import os

result_dir = '.\\test_project\\report'

lists = os.listdir(result_dir)

#sort file by time
lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))

print(('最新的文件为： ' + lists[-1]))
file = os.path.join(result_dir, lists[-1])
print(file)
