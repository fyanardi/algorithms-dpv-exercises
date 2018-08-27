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
    T = [ p_ for p_ in p ]
    for i in range(len(m)):
        for j in range(i):
            if (m[i] - m[j]) > k:
                T[i] = max(T[i], p[i] + T[j])

    max_ = 0
    for i in range(len(m)):
        if T[i] > T[max_]:
            max_ = i
    return T[max_]


if __name__ == "__main__":
    m = [ 2, 5, 6, 11, 14, 20, 22, 28 ];
    p = [ 10, 30, 40, 1, 15, 5, 23, 17 ];
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
