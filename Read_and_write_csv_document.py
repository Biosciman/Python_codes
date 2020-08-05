import csv

# 读取list1文件
List1 = csv.reader(open('Read_and_write_csv_document_list1.csv', 'r'))
list1 = []
for i in List1:
    list1.append(i)
list1 = list1[1:]

# 提取list1中第二列
list11 = []
for i in list1:
    list11.append(i[1])

# 读取list2文件
List2 = csv.reader(open('Read_and_write_csv_document_list2.csv', 'r'))
list2 = []
for i in List2:
    list2.append(i)
list2 = list2[1:]

# 提取list2中第二列
list21 = []
for i in list1:
    list21.append(i[1])

# 将list11和list21做差集（list11中有，而list21中没有）
DifferenceList = list(set(list11).difference(set(list21)))

# 将list11和list21做交集
IntersectionList = list(set(list11).intersection(set(list21)))

# 将list11和list21做并集
UnionList = list(set(list11).union(set(list21)))

# 将交集IntersectionList写入新csv文件
with open('Read_and_write_csv_document_list1_list2_intersection.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow(['Chemical Name', 'CAS Number'])
    for i in list1:
        if i[1] in IntersectionList:
            writer.writerow(i)