import numpy as np


def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    # Initialise
    result = []
    for i in range(len(choices)):
        result.append(0)
    resultArray = np.array(result)
    memo = {}
    choicesCopy = choices[:]

    
    print(resultArray)
    for i in range(len(choices)):
        if choices[i] > total:

            break
        elif choices[i] <= total:
            result[i] = 1
            total -= choices[i]
            choicesCopy[i] = 0




# Test 1
choices = [1, 2, 2, 3]
total = 4
print(find_combination(choices, total))

# Test 2
choices = [1, 1, 3, 5, 3]
total = 5
print(find_combination(choices, total))

# Test 3
choices = [1, 1, 1, 9]
total = 4
print(find_combination(choices, total))

