from ast import Index


with open('cv07.txt') as text_file:
    my_text = list(text_file.read())
    my_text.sort()

result = []

for i in my_text:
    if i not in result:
        result.append(i)
        result.append(1)
    else:
        result[result.index(i) + 1] += 1


print(result)