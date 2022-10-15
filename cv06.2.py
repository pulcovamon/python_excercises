from operator import index
import string


my_string = 'Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies.'
my_list = my_string.split()
result = []

for i in my_list:
    if i not in result:
        result.append(i)
        result.append(1)
    else:
        result[result.index(i) + 1] += 1

print(result)