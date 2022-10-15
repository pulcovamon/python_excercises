my_string = 'Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies.'
my_list = my_string.split() # bylo by lepší použít tuhle funkci, ale už to mám jinak žejo

word = ''
all_words = []

for i in range(len(my_string)):
    if my_string[i] != ' ' and my_string[i] != '.' and my_list[i] != ',':
        word = word + my_string[i]
        #print(word)
    else:
        if word not in all_words:
            all_words.append(word)
            all_words.append(1)
        else:
            all_words[all_words.index(word) + 1] += 1
        word = ''

print(all_words)