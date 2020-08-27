import pandas as pd
import numpy as np

# 以下是某有限责任公司一组销售数据，请利用pandas数据透视表相关知识按要求进行统计分析
# 利用 pandas 读取 task6_1.csv 文件中的数据，建立 DataFrame
Dataframe = pd.read_csv('task6_1.csv')
# 利用 pivot_table 统计该企业每个人每天销售商品 A 和 B 的金额之和
pd.pivot_table(Dataframe, index=['id', 'date'], values=['sales'], aggfunc=np.sum)
# 请将上面的统计数据再增加一列，统计出每个人的销售总金额
pd.pivot_table(Dataframe, index=['id', ], values=['sales'], columns=['date'],
                     aggfunc=np.sum,  margins=True, fill_value=0)

# 以下为部分抽烟人群调查表，请将数据存储入 DataFrame，并完成以下操作
# 利用 pandas 读取 task6_2.csv 文件中的数据，建立 DataFrame
df = pd.read_csv('task6_2.csv')
# 请以性别为分组依据，查看男女抽烟平均年龄和身高
df['sex'] = df['sex'].astype('category')
df['sex'].cat.set_categories(['man', 'women'], inplace=True)
pd.pivot_table(df, index=['sex'], values=['age', 'height'], aggfunc=np.mean)
# 利用交叉表知识，统计各个性别抽烟的人数
pd.crosstab(index=[df['sex']], columns=[df['smoke']], margins=True)
# 利用交叉表知识，统计各个年龄段抽烟人情况
a = pd.crosstab(df.age, df.smoke)
print(a)