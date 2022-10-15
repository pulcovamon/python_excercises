import random

arr1 = random.sample(range(-10, 10), 10)
arr1.sort()
arr2 = random.sample(range(-10, 10), 10)
arr2.sort()
arr3 = random.sample(range(-10, 10), 10)
arr3.sort()
target = 5

combinations = []

for number in arr1:
    index2 = 0
    index3 = len(arr3) - 1
    found = False

    while not found:
        three_elements = [number, arr2[index2], arr3[index3]]
        my_sum = sum(three_elements)
        if my_sum == target:
            combinations.append(three_elements)
            found = True
        elif my_sum < target:
            index2 += 1
        else:
            index3 -= 1

print(combinations)