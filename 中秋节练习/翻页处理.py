import re

str = '共100页'
x = re.findall('\d+', str)
print(x)

y = re.findall('\d+', str)[0]
print(y)
print(type(y))