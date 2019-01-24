"""
6.7 A subsequence is palindromic if it is the same whether read left to right or right to left. For
instance, the sequence
            A, C, G, T, G, T, C, A, A, A, A, T, C, G
has many palindromic subsequences, including A, C, G, C, A and A, A, A, A (on the other hand, the
subsequence A, C, T is not palindromic). Devise an algorithm that takes a sequence x[1...n] and
returns the (length of the) longest palindromic subsequence. Its running time should be O(n^2).
"""

def palindromic_subsequence(x):
    """
    Returns the length of the longest palindromic subsequence in a sequence x
    expression is a, False otherwise
    Args:
        x: string containing palindromic subsequences
    """
    T = [[ 0 for i in x] for j in x]
    n = len(x)
    for i in range(n):
        T[i][i] = 1

    for s in range(n):
        for i in range(n - s):
            j = i + s
            if x[i] == x[j]:
                if i + 1 == j:
                    T[i][j] = 2
                elif i + i < j:
                    T[i][j] = 2 + T[i+1][j-1]
            else:
                T[i][j] = max(T[i][j-1], T[i+1][j])
            """
            if i + 1 < j:
                if x[i] == x[j]:
                    T[i][j] = 2 + T[i+1][j-1]
                else:
                    T[i][j] = max(T[i][j-1], T[i+1][j])
            elif i + 1 == j:
                if x[i] == x[j]:
                    T[i][j] = 2
                else:
                    T[i][j] = 1
            """
            # print('i=%d j=%d x[i..j]=%s T=%d' % (i, j, x[i:j+1], T[i][j]))

    return T[0][n-1]


if __name__ == "__main__":
    # test case from exercise 6.7
    x = 'ACGTGTCAAAATCG'
    l = palindromic_subsequence(x)
    print('x=[%s] l=%s' % (x, l))

    x = 'A'
    l = palindromic_subsequence(x)
    print('x=[%s] l=%s' % (x, l))

    x = 'AB'
    l = palindromic_subsequence(x)
    print('x=[%s] l=%s' % (x, l))

    x = 'BB'
    l = palindromic_subsequence(x)
    print('x=[%s] l=%s' % (x, l))

    x = 'BAB'
    l = palindromic_subsequence(x)
    print('x=[%s] l=%s' % (x, l))

