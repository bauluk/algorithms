import random

def mergeSort(numbers):
    if len(numbers) <= 1:
        return numbers

    left = numbers[:len(numbers)//2]
    right = numbers[len(numbers)//2:]
    left = mergeSort(left)
    right = mergeSort(right)
    numbers = merge(left, right, numbers)

    return numbers

def merge(left, right, numbers):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k +=1
    # process any leftovers
    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k +=1
    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k +=1

    return numbers

numbers = []
for i in range(0, 100):
    numbers.append(random.randint(1, 100))

numbers = mergeSort(numbers)
print(numbers)
