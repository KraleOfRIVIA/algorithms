def sum(array):
    if len(array) < 2:
        return array[0]
    else:
        return array[0] + sum(array[1:])
print(sum([5,2,5,8,9]))