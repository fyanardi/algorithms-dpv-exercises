"""
6.17 Given an unlimited supply of coins of denominations x1,x2,...xxn, we wish to make change for a
value v; that is, we wish to find a set of coins whose total value is v. This might not be possible,
for instance, if the denominations are 5 and 10 then we can make change for 15 but not for 12. Give
an O(nv) dynamic-programming algorithm for the following problem.
    Input: x1,...xn;v.
    Question: Is it possible to make change for v using coins of denominations x1,...,xn?
"""

def coin_change_unlimited(x, v):
    """
    Returns True if is possible to make change for v using coins of denominations x1...xn, False
    Args:
        x: array of coins of denominations x1, x2 ... xn
        v: change value
    """
    n = len(x)

    C = [ False for i in range(v+1) ]
    # Base case C(0) = True
    C[0] = True

    for i in range(1, v+1):
        for j in range(n):
            if i >= x[j]:
                C[i] = C[i-x[j]]
                if C[i]:
                    break

    return C[v]


if __name__ == "__main__":
    x = [ 5, 10 ]
    v = 15
    c = coin_change_unlimited(x, v)
    print('x=%s v=%d change: %s' % (x, v, c))

    x = [ 5, 10 ]
    v = 12
    c = coin_change_unlimited(x, v)
    print('x=%s v=%d change: %s' % (x, v, c))

    x = [ 2, 10 ]
    v = 9
    c = coin_change_unlimited(x, v)
    print('x=%s v=%d change: %s' % (x, v, c))

