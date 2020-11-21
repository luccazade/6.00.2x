def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    max_so_far = 0
    max_ending_here = 0

    for i in range(len(L)):
        max_ending_here = max_ending_here + L[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


# TESTS

print(max_contig_sum([3, 4, -1, 5, -4]))

print(max_contig_sum([3, 4, -8, 15, -1, 2]))
