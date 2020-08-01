import math
import random

def binarySearchAlgorithm(numbers, target):
    smallest = 0
    largest = len(numbers) - 1
    iterations = 0
    while smallest <= largest:
        iterations += 1
        index = (smallest + largest) // 2
        if numbers[index] < target:
            smallest = index + 1
        elif numbers[index] > target:
            largest = index - 1
        else:
            return True, index, iterations

    return False, None, iterations

numbers = []
for i in range(0, 1000):
    numbers.append(random.randint(1, 1000))

numbers = sorted(numbers)
target = random.randint(1, 1000)
success, index, iterations = binarySearchAlgorithm(numbers, target)

if success is True:
    print('Target (' + str(target) + ') was found at index [' + str(index) + '] after ' + str(iterations) + ' iterations.')
else:
    print('Target (' + str(target) + ') failed to be found after ' + str(iterations) + ' iterations, because it does not exist within the list.')
