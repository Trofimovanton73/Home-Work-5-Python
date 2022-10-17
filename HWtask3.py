# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

def notEven(col):
    newList=[]
    for i in range(len(col)):
        if (i%2==1):
            newList.append(col[i])
    return newList
myList = list([random.randint(1,99) for i in range(6)])
print(myList)
# res = notEven(myList) 
# print(res)
# sumOfElements = sum(res)
sumOfElements = notEven(lambda i: (i, sum(myList)), myList)
print (sumOfElements)