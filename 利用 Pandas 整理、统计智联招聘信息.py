import pandas as pd

# 读取 CSV 格式文件“task_1_zhaopin_data.csv” (阅读参考文献 4)，并展示所有数据，数据名为为 df1;
filename = 'task_1_zhaopin_data.csv'
df1 = pd.read_csv(filename)

# 利用 head 选取前部数据查看 (阅读参考文献 5);
print(df1.head())

# 利用 tail 选取底部数据查看 (阅读参考文献 5);
print(df1.tail())

# 选取前 3 行数据查看 (阅读参考文献 5);
print(df1.head(3))

# 选取第 3 行数据查看 (阅读参考文献 5);
print(df1[2:3])

# 选取【学历要求】、【工作经验】、【是否全职】3 列 (阅读参考文献 6);
print(df1[['学历要求', '工作经验', '是否全职']])

# 将【公司名】设置为 index 索引 (阅读参考文献 7)，并将表格重新命名为 df2;
df2 = df1.set_index('公司名')

# 在 df2 上删除指定列【其他备注】(阅读参考文献 8)，并命名新表为 df3;
df3 = df2.drop('其他备注', axis=1)

# 在 df3 上删除指定行数据，“上海蜗兴科技有限公司”所在行 (阅读参考文献 8)，并将数据命名为 df4;
df4 = df3.drop('上海蜗兴科技有限公司')

# 保存 df4 为 CSV 格式文件，并把被保存的 CSV 格式文件命名为“task_1_zhaopin_data_update.csv (阅读参考 文献 9)”。
df4.to_csv('task_1_zhaopin_data_update.csv')