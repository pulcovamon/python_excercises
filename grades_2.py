# better solution
if __name__ == '__main__':
    students = ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']    # simulates user input
    scores = [37.21, 37.21, 37.2, 41., 39.]

    grades = []

    for i in range(5):
        name = students[i]
        score = scores[i]
        grades.append([name, score])

grades = [i for i in grades if i[1] != min([j[1] for j in grades])]
grades = [i[0] for i in grades if i[1] == min([j[1] for j in grades])]
grades.sort()

print('\n'.join(grades))