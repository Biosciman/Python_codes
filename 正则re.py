import re

"""
- .(点号)：表示任意一个字符，除了\n，比如查找所有的一个字符 \.
- []：匹配中括号中列举的任意字符
- \d：任意一个数字
- \D：除了数字都可以
- \s：表示空格，tab键
- \S：除了空白符号
- \w：单词字符，a-z, A-Z, 0-9,
 - \W：除了\w的字符
- *：表示前面内容重复零次或者多次
- +：表示前面内容至少出现一次
- ？：前面才出现的内容零次或者一次
- {m, n}：允许前面内容出现最少m次，最多n次
- ^：匹配字符串的开始
- $：匹配字符串的结尾
- \b：匹配单词的边界
- （）：对正则表达式内容进行分组，从第一个括号开始，编号逐渐增大
          验证一个数字： ^\d$
          必须有一个数字，最少一位：^\d+$
          只能出现数字，且位数为5-10位：^\d{5, 10}$
          注册者输入年龄，要求16岁以上，99岁以下：^[16-99]$
          只能输入英文字符和数字：^[A-Za-z0-9]$
          验证QQ号码：[0-9]{5, 12}
- \A：只匹配字符串开头，\Aabcd，则abcd
- \Z：仅匹配字符串末尾，abcd\Z，abcd
- |：左右任意一个
- (?P<name>...)：分组，除了原来的编号再制定一个别名
-(?p=name)：引用分组
"""

p = re.compile(r'(\w+) (\w+)')

s = "I am Linus Torvalds."

# search查找
rst = p.search(s)
# print(rst)
# print(rst.group())
# print(rst.groups())

# findall
rst = p.findall(s)
# print(type(rst))
# print(rst)

# sub替换
rst = p.sub(r'Hello world', s)
# print(rst)

# 匹配中文
# 大部分中文内容表示范围是[u4e00-u9fa5]，不包括全角标点
s2 = u"我是:林纳斯托瓦兹。"
p = re.compile(r'[\u4e00-\u9fa5]+')
rst = p.findall(s2)
# print(rst)

# 贪婪和非贪婪
# 贪婪：尽可能多的匹配，（*）表示贪婪匹配
# 非贪婪：找到符合条件的最小内容即可，(?)表示非贪婪
# 正则默认使用贪婪匹配

s3 = u'<div>name</div><div>age</div>'

p1 = re.compile(r'<div>.*</div>')
p2 = re.compile(r'<div>.*?</div>')

rst1 = p1.search(s3)
rst2 = p2.search(s3)
# print(rst1.group())
# print(rst2.group())