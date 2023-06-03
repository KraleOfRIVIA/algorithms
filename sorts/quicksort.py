import random
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = random.choice(array) # берем случайный элемент как опорный для улучшения среднего времени работы
        less = [i for i in array if i<pivot]
        greater = [i for i in array if i>pivot]
    return quicksort(less)+ [pivot] + quicksort(greater)
print(quicksort([4,3,7,10,15,60]))
