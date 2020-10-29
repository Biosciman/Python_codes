import csv
import pandas as pd

csv_data = pd.read_csv('CL20101019.csv', header=None)

# print(csv_data.head(5))
# print(csv_data[1])

list1 = []
for i in range(3392):
    list2 = []
    for j in csv_data[i]:
        list2.append(j)
    list1.append(list2)

list1 = list1[1:]

# list3 = []
# for i in list1[0]:
#     list3.append(i.split(','))
# list4 = list3[1:]
# print(list4)

list5 = []
for i in list1:
    list3 = []
    for j in i:
        list3.append(j.split(','))
    list5.append(list3)

for i in list5:
