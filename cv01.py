from logging import raiseExceptions


def different(sequence):

    if not isinstance(sequence, list):
        raise Exception('Not a list!')

    sequence.sort()
    for j in range(len(sequence)-1):
        if sequence[j] == sequence[j+1]:
            return 'same numbers'

    return 'different numbers'

numbers = 5
same_or_different = different(numbers)
print(same_or_different)