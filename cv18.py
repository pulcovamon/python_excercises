numbers = [-0.098, 0.105, 0.002, -0.012, -0.085, 0.004, -0.073, 0.112, 1.995, 0.025]

def median_function(data):
    data.sort()

    n = len(data)

    if n % 2 == 0:
        median = (data[int(n/2)] + data[int(n/2)+1]) / 2
    else:
        median = data[int((n+1)/2)]
    
    return median

print(median_function(numbers))