"""
6.8 Given two strings x = x_1 x_2 ... x_n and y = y_1 y_2 ... y_m we wish to find the length of
their longest common substring, that is, the largest k for which there are indices i and j with
x_i x_i+1 ... x_i+k-1 = y_j y_j+1 ... y_j+k-1. Show how to do this in time O(mn).
"""

def longest_common_substring(x, y):
    """
    Returns the length of the longest common substring from two strings x and y
    Args:
        x, y: two string whose longest common substring to be computed
    """

    # Simpler version that uses indices 1...n-1 instead of 1...n as devised by the DP alg.
    # This requires additional checking for i=0 and j=0
    n = len(x)
    m = len(y)
    T = [[ 0 for i in y] for j in x]

    for i in range(n):
        for j in range(m):
            if x[i] == y[j]:
                if i > 0 and j > 0:
                    T[i][j] = 1 + T[i][j]
                else:
                    T[i][j] = 1
            else:
                T[i][j] = 0

    # Can combine this loop with the table-building loop above
    max_ = 0
    for i in range(n):
        for j in range(m):
            if T[i][j] > max_:
                max_ = T[i][j]
    return max_

    """
    n = len(x)
    m = len(y)
    T = [[ 0 for i in range(0, m+1)] for j in range(0, n+1)]

    for i in range(n):
        T[i][0] = 0
    for j in range(m):
        T[0][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                T[i-1][j-1] = 1 + T[i-2][j-2]
            else:
                T[i-1][j-1] = 0

    max_ = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if T[i][j] > max_:
                max_ = T[i][j]
    return max_
    """


if __name__ == "__main__":
    # Test cases from www.geeksforgeeks.org
    x = "GeeksforGeeks"
    y = "GeeksQuiz"
    l = longest_common_substring(x, y)
    print('x=[%s] y=[%s] l=%d' % (x, y, l))

    x = "abcdxyz"
    y = "xyzabcd"
    l = longest_common_substring(x, y)
    print('x=[%s] y=[%s] l=%d' % (x, y, l))

    x = "zxabcdezy"
    y = "yzabcdezx"
    l = longest_common_substring(x, y)
    print('x=[%s] y=[%s] l=%d' % (x, y, l))

    # Edge cases
    x = "abcdefgh"
    y = "zxy"
    l = longest_common_substring(x, y)
    print('x=[%s] y=[%s] l=%d' % (x, y, l))

    x = "a"
    y = "a"
    l = longest_common_substring(x, y)
    print('x=[%s] y=[%s] l=%d' % (x, y, l))

    x = "a"
    y = "b"
    l = longest_common_substring(x, y)
    print('x=[%s] y=[%s] l=%d' % (x, y, l))
