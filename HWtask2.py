from random import randint as rI

uniqueList = {}
finalStr = ''

# listStr=[]
# for i in range (20):
#     listStr.append(rI(0, 9))
# for i in range (len(listStr)):
#     listStr[i] = str (listStr[i])
# listStr = ''.join(listStr)
listStr = ''.join(list(map(str,[rI(0,9) for i in range(20)])))

print(f'Задана последовательность цифр: {listStr}')

for a in listStr:
    if uniqueList.get(a):
        uniqueList[a] = uniqueList.get(a) + 1
    else:
        uniqueList[a] = 1
print(uniqueList)

for i in uniqueList.items():
    if i[1]==1:
        finalStr +=str (i[0]) + ' '
print(f'Уникальные цифры {finalStr}') if finalStr else print('Уникальных позиций нет')