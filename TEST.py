import pandas as pd
from scipy import stats

filename = '/Users/zhangliming/Documents/Tsinghua University/现代生物学技术/学生统计.csv'
df = pd.read_csv(filename)
df.loc[df['性别'] == '男', '性别'] = 1
df.loc[df['性别'] == '女', '性别'] = 0
df = df[['性别', '猜测老师年龄/岁']]
df = df.dropna(how='all')
rst = stats.pointbiserialr(df['性别'], df['猜测老师年龄/岁'])
help(scipy)