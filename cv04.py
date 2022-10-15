from re import M


my_list = [1, 3, -5, 4, -8, 12, 6, -4, -1, 9, 7, -9]

triplets_zero = []

for i in range(len(my_list)-1):
    for j in range(len(my_list)-1):
        for k in range(len(my_list)-1):
            if i != j and i != k and j != k:
                triplet = [my_list[i], my_list[j], my_list[k]]
                my_sum = sum(triplet)
                if my_sum == 0:
                    triplets_zero.append(triplet)

print(triplets_zero)


k=[x**2 for x in range(10)]
print(k)