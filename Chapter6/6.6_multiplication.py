"""
6.6 Let us define a multiplication operation on three symbols a, b, c according to the following
table; thus ab = b, ba = c and so on. Notice the multiplication operation defined by the table is
neither associative nor commutative.
            | a b c
          --|------
          a | b b a
          b | c b a
          c | a c c
Find and efficient algorithm that examines a string of these symbols, say bbbbac, and decides
whether or not it is possible to parenthesize the string in such a way that the value of the
resulting expression is a. For example, on input bbbbac your algorithm should return yes because
((b(bb))(ba))c = a
"""

def multiplication(s):
    """
    Returns True if is possible to parenthesize the string in such a way the the value resulting
    expression is a, False otherwise
    Args:
        s: string containing 'a', 'b', and 'c'
    """
    n = len(s)
    # M is a 3 dimensional array, ixj and every M[i,j] is also an array containing possible result
    # of evaluating substring i to j
    M = [[[] for i in s] for j in s]
    # Base case M(i, i) = s(i)
    for i in range(n):
        M[i][i] = [s[i]]

    # Must fill in the table diagonally from M(i, i+1) till M(1, n)
    # Here w denotes the diagonal width, which is n-1
    for w in range(1, n):
        # print('*** w=%d ***' % w)
        for i in range(n-w):
            j = i + w
            # print('** i=%d j=%d **' % (i, j))
            for l in range(i, j):
                # print('* l=%d M[%d][%d] *' % (l, i, j))
                # print('  M[i][l]=%s M[l+1][j]=%s' % (M[i][l], M[l+1][j]))
                m = __mul(M[i][l], M[l+1][j])
                M[i][j] = __merge(M[i][j], m)

    return 'a' in M[0][n-1]


def __mul(m1, m2):
    r = []
    for m1_ in m1:
        for m2_ in m2:
            m = ''
            if m1_ == 'a' and m2_ == 'a':
                m = 'b'
            elif m1_ == 'a' and m2_ == 'b':
                m = 'b'
            elif m1_ == 'a' and m2_ == 'c':
                m = 'c'
            elif m1_ == 'b' and m2_ == 'a':
                m = 'c'
            elif m1_ == 'b' and m2_ == 'b':
                m = 'b'
            elif m1_ == 'b' and m2_ == 'c':
                m = 'a'
            elif m1_ == 'c' and m2_ == 'a':
                m = 'a'
            elif m1_ == 'c' and m2_ == 'b':
                m = 'c'
            elif m1_ == 'c' and m2_ == 'c':
                m = 'c'
            if m not in r:
                r.append(m)

    return r


def __merge(m1, m2):
    for m in m2:
        if m not in m1:
            m1.append(m)

    return m1


if __name__ == "__main__":
    s = 'bbbbac'
    m = multiplication(s)
    print('s=[%s] m=%s' % (s, m))

    s = 'bbbbbb'
    m = multiplication(s)
    print('s=[%s] m=%s' % (s, m))

    s = 'baab'
    m = multiplication(s)
    print('s=[%s] m=%s' % (s, m))

    s = 'aabc'
    m = multiplication(s)
    print('s=[%s] m=%s' % (s, m))

