"""
6.18 Consider the following variation on the change-making problem (Exercise 6.17): you are given
denominations x1,x2,...,xn, and you want to make change for a value v, but you are allowed to use
each denomination at most once. For instance, if the denominations are 1, 5, 10, 20, then you can
make change for 16 = 1 + 15 and for 31 = 1 + 10 + 20 but not for 40 (because you can't use 20
twice).
    Input: Positive integers x1,x2,...,xn; another integer v.
    Output: Can you make change for v, using each denomination xi at most once?
Show how to solve this problem in time O(nv).
"""

def coin_change_once_per_denomination(x, v):
    """
    Returns True if is possible to make change for v using coins of denominations x1...xn and each
    denomination is used once, False otherwise
    Args:
        x: array of coins of denominations x1, x2 ... xn
        v: change value
    """
    n = len(x)

    C = [[False for j in range(v+1)] for i in range(n+1)]
    # Base case C(i, 0) = True
    for i in range(n+1):
        C[i][0] = True

    for i in range(1, n+1):
        for j in range(v+1):
            if x[i-1] <= j:
                C[i][j] = C[i-1][j-x[i-1]] or C[i-1][j]
            else:
                C[i][j] = C[i-1][j]

    return C[n][v]


if __name__ == "__main__":
    x = [5, 10]
    v = 15
    c = coin_change_once_per_denomination(x, v)
    print('x=%s v=%d change: %s' % (x, v, c))

    x = [1, 5, 10, 20]
    v = 16
    c = coin_change_once_per_denomination(x, v)
    print('x=%s v=%d change: %s' % (x, v, c))

    x = [1, 5, 10, 20]
    v = 31
    c = coin_change_once_per_denomination(x, v)
    print('x=%s v=%d change: %s' % (x, v, c))

    x = [1, 5, 10, 20]
    v = 40
    c = coin_change_once_per_denomination(x, v)
    print('x=%s v=%d change: %s' % (x, v, c))

    x = [1, 5, 10, 20]
    v = 21
    c = coin_change_once_per_denomination(x, v)
    print('x=%s v=%d change: %s' % (x, v, c))

    x = [1, 5, 10, 20]
    v = 38
    c = coin_change_once_per_denomination(x, v)
    print('x=%s v=%d change: %s' % (x, v, c))

