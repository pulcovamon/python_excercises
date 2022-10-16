import copy

if __name__ == '__main__':

    students = ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']    # simulates user input
    scores = [37.21, 37.21, 37.2, 41., 39.]

    names_second_lowest = []
    name_lowest = []
    lowest = float('inf')
    second_lowest = float('inf')
    
    for i in range(5):
        name = students[i]
        score = scores[i]
        
        if score < lowest:
            second_lowest = lowest
            lowest = score
            names_second_lowest = copy.deepcopy(name_lowest)
            name_lowest.clear()
            name_lowest.append(name)
        elif score < second_lowest and score != lowest:
            second_lowest = score
            names_second_lowest.clear()
            names_second_lowest.append(name)
        elif score == second_lowest:
            names_second_lowest.append(name)
        elif score == lowest:
            name_lowest.append(name)

    names_second_lowest.sort()
    
    print('\n'.join(names_second_lowest))