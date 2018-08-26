"""
6.1 A contiguous subsequence of a list S is a subsequence made up of consecutive elements of S. For
instance, if S is:
    5. 15, -30, 10, -5, 40, 10
then 15, -30, 10 is a contiguous subsequence but 5, 15, 40 is not. Give a linear time algorithm for
the following task:
    Input: A list of numbers, a1, a2, ..., an
    Output: The contiguous subsequence of maximum sum (a subsequence of length zero has sum zero)
For the preceeding example, the answer would be 10, -5, 40, 10, with a sum of 55.
(Hint: For each j E{1, 2, ..., n}, consider contiguous subsequences ending exactly at position j.)
"""

"""
v1: Returns the contiguous subsequence with maximum sum.
"""
def contiguous_subseq_max_sum_1(a):
    S = [ 0 for i in a ]
    l = [ 0 for i in a ]
    for i in range(len(a)):
        if a[i] + S[i - 1] > a[i]:
            S[i] = a[i] + S[i - 1]
            l[i] = l[i - 1]
        else:
            S[i] = a[i]
            l[i] = i

    max = 0
    for i in range(len(a)):
        if S[i] > S[max]:
            max = i

    return a[l[i]:max+1]


"""
v2: Returns only the sum of the contiguous subsequence with maximum sum
"""
def contiguous_subseq_max_sum_2(a):
    S = [ 0 for i in a ]
    for i in range(len(a)):
        S[i] = max(S[i], a[i] + S[i - 1])

    max_ = 0
    for i in range(len(a)):
        if S[i] > S[max_]:
            max_ = i

    return S[max_]


if __name__ == "__main__":
    a = [ 5, 15, -30, 10, -5, 40, 10 ]
    s = contiguous_subseq_max_sum_1(a)
    print('Contiguous subsequence with max sum => %s' % s)
    sum = contiguous_subseq_max_sum_2(a)
    print('Max sum => %s' % sum)

