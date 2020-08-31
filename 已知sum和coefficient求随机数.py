import random
miR33a = 120*1.93
miR29c = 120*1.34
miR126 = 120*1.64

single = 23 # 1.75
two = 53 # 1.95
multiple = 44 # 2.0



result = 0

while result == 0:
    miR33a1 = float('%.2f' % random.random())+1
    miR33a2 = float('%.2f' % random.random())+1
    miR33a3 = float('%.2f' % random.random())+1
    if miR33a1 < miR33a2 and miR33a2 < miR33a3:
        if single*miR33a1 + two*miR33a2 + multiple*miR33a3 == miR33a:
            result = 1
        else:
            continue
    else:
        continue



print(miR33a1)
print(miR33a2)
print(miR33a3)
print('*'*30)

