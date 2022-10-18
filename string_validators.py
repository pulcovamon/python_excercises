if __name__ == '__main__':
    s = 'qA2'
    
    counts = [False] * 5
    
    for i in s:
        if not counts[0] and i.isalnum():
            counts[0] = True
            
        if not counts[1] and i.isalpha():
            counts[1] = True
            
        if not counts[2] and i.isdigit():
            counts[2] = True
            
        if not counts[3] and i.islower():
            counts[3] = True
            
        if not counts[4] and i.isupper():
            counts[4] = True
            
    print(*counts, sep = '\n')