def swap_case(s):
    
    new_text = ''

    for i in s:
        if i.islower():
            new_text += i.upper()
        elif i.isupper():
            new_text += i.lower()
        else:
            new_text += i

    return new_text

if __name__ == '__main__':
    
    text = 'HackerRank.com presents "Pythonist 2".'
    print(swap_case(text))