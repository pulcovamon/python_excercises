# 1st result
n = 5
arr = map(int, '2 3 6 6 5'.split())

score1 = list({i for i in arr})
score1.sort()
print(score1[-2])

# 2nd result
n = 5
arr = map(int, '2 3 6 6 5'.split())

score2 = [i for i in arr]
score2 = [i for i in score2 if i != max(score2)]
print(max(score2))

# 3rd result
n = 5
arr = map(int, '2 3 6 6 5 7 8 8 10'.split())

first = 0
second = 0
for i in arr:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i
print(second)