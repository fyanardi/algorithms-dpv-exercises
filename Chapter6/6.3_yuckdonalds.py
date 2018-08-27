"""
6.3 Yuckdonald's is considering open a series of restaurants along Quant Valley Highway (QVH). The
n possible locations are along a straight line, and the distances of these locations are along a
straight line, and the distance of these locations from the start of QVH are, in miles and in
increasing order, m1, m2, ..., mn. The constraints are as follows:

* At each location, Yuckdonald's may open at most one restaurant. The expected profit from opening
  a restaurant at location i is pi, where pi > 0 and i = 1, 2, ..., n.
* Any two restaurants should be at least k miles apart, where k is a positive integer.

Give an efficient algorithm to compute the maximum expected total profit subject to the given
constraints.
"""

"""
Returns the maximum expected total profit
"""
def yuckdonalds(m, p, k):
    # Start from 0 for convenience
    # is the maximum profit at each location, initialize to be the profit at each location
    T = [ 0 for p_ in p ]
    for i in range(len(m)):
        T[i] = p[i]
        for j in range(i - 1):
            if (m[i] - m[j]) >= k:
                T[i] = max(T[i], p[i] + T[j])

        # Final maximum profit is the maximum when there is a restaurant at i and maximum profit
        # when there is no restaurant at position i, given recursively by T[i-1]
        T[i] = max(T[i], T[i-1])

    return T[len(m)-1]


"""
Another version:
    Here T(i) is the maximum total profit when there is a restaurant at location i.
    For this version, we need to perform one more iteration to find at which location where there
    is a restaurant the total expected profit is maximum
"""
"""
def yuckdonalds(m, p, k):
    # Start from 0 for convenience
    # is the maximum profit at each location, initialize to be the profit at each location
    T = [ 0 for p_ in p ]
    for i in range(len(m)):
        T[i] = p[i]
        for j in range(i - 1):
            if (m[i] - m[j]) >= k:
                T[i] = max(T[i], p[i] + T[j])

    max_ = 0
    for i in range(len(m)):
        if T[i] > T[max_]:
            max_ = i
    return T[max_]
"""


if __name__ == "__main__":
    m = [ 0, 5, 6, 11, 14, 20, 22, 28 ];
    p = [ 30, 10, 40, 1, 15, 5, 23, 17 ];
    k = 5;
    print('m=%s p=%s k=%s' % (m, p, k))
    p_ = yuckdonalds(m, p, k)
    print('Maximum total profit = %d' % p_)

    m = [ 1, 10, 16, 21, 22, 35, 38 ]
    p = [ 30, 9, 13, 25, 23, 3, 10 ]
    k = 10
    print('m=%s p=%s k=%s' % (m, p, k))
    p_ = yuckdonalds(m, p, k)
    print('Maximum total profit = %d' % p_)

    # Greedy approach (which assumes a restaurant at location i) will fail this case (correct
    # answer is 400)
    m = [ 10, 20, 25, 30, 40 ];
    p = [ 100, 100, 101, 100, 100 ];
    k = 10;
    print('m=%s p=%s k=%s' % (m, p, k))
    p_ = yuckdonalds(m, p, k)
    print('Maximum total profit = %d' % p_)

    # Corner case, the return should be 42 and not 41
    m = [ 0, 4, 8 ];
    p = [ 10, 42, 31 ];
    k = 5;
    print('m=%s p=%s k=%s' % (m, p, k))
    p_ = yuckdonalds(m, p, k)
    print('Maximum total profit = %d' % p_)

