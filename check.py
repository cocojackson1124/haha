import collections #创建一个新的容器
f = open('D:/Walden.txt', 'r').read() #打开本地文本文件，r表示以读取方式打开
f=f.replace(',','').replace('.','').replace('"','').replace(':','') #将所有标点替换成空格
f = f.split() #取出所有单词
f = collections.Counter(f) #在容器中统计每个单词的出现词频
print(f)
