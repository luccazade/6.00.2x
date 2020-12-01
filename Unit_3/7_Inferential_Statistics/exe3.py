def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    import math
    n = len(L)
    if n == 0:
        return 'NaN'
    lengths = []
    tot = 0
    for i in L:
        lengths.append(len(i))
        tot += len(i)
    mean = tot / n
    summation = 0
    for i in lengths:
        summation += (i - mean) ** 2
    stdDev = math.sqrt(summation / n)
    return stdDev


L = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L))
