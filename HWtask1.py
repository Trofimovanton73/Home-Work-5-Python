# Реализуйте алгоритм перемешивания списка.

import random

# myList = [] 
# for i in range(6):
#     myList.append(random.randint(1, 99))
myList = list([random.randint(1, 99) for i in range(6)])

print(f"Исходный список: {myList}")  

for i in range (len(myList)):
    j = random.randint(0, i)    
    myList[i], myList[j] = myList[j], myList[i]

print(f"Измененный список: {myList}")