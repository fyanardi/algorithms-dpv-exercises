"""
6.5 We are given a checkerboard which has 4 rows and n columns, and has an integer written in each
square. We are also given a set of 2n pebbles, and we want to place some or all of these on the
checkerboard (each pebble can be placed on exactly one square) so as to maximize the sum of the
integers in the squares that are covered by pebbles. There is one constraint: for a placement of
pebbles to be legal, no two of them can be on horizontally or vertically adjacent squares (diagonal
adjacency is ok).

(a) Determine the number of legal patterns that can occur in any column (in isolation, ignoring the
    pebbles in adjacent columns) and describe these patterns.

Call two patterns compatible if they can be placed on adjacent columns to form a legal placement.
Let us consider subproblems consisting of the rst k columns 1 k n. Each subproblem can be assigned a
type, which is the pattern occurring in the last column.

(b) Using the notions of compatibility and type, give an O(n)-time dynamic programming algorithm
for computing an optimal placement.
"""

"""
All possible patterns and for each pattern, the corresponding compatible patterns (in pattern index)
For each tuple:
    First entry is row(s) to have pebbles
    Second entry is the compatible pattern indices
"""
PATTERNS = [
        ([], [0, 1, 2, 3, 4, 5, 6, 7]), # type 0
        ([0], [0, 2, 3, 4, 7]),         # type 1
        ([1], [0, 1, 3, 4, 5]),         # type 2
        ([2], [0, 1, 2, 4, 7]),         # type 3
        ([3], [0, 2, 3, 5]),            # type 4
        ([0, 2], [0, 2, 4, 7]),
        ([0, 3], [2, 3]),
        ([1, 3], [5])
]

def max_sum_checkerboard_pebbles(c):
    """
    Args:
        c: array representation of a checkerboard with size 4 rows x n columns. The array's first
            dimension is the checkerboard's 4 rows, and every row contains n columns.
    """
    # S is an array or n columns and 8 rows
    n = len(c[0])
    S = [[0 for c in range(n)] for r in range(8)]
    # Iterate over column
    for i in range(n):
        # print('* i=%d *' % i)
        # Then iterate over all possible pattern
        for j in range(8):
            # print('j=%d pattern=%s compatible=%s' % (j, PATTERNS[j][0], PATTERNS[j][1]))
            max_ = 0
            if i > 0:
                for k in PATTERNS[j][1]:
                    # print(' S[%d][%d]=%d' % (k, i, S[k][i-1]))
                    max_ = max(max_, S[k][i-1])
            S[j][i] = __sum(c, i, PATTERNS[j][0]) + max_
            # print('=> S[%d][%d]=%d' % (j, i, S[j][i]))

    max_ = 0
    for i in range(8):
        max_ = max(max_, S[i][n-1])

    return max_


def __sum(c, i, p):
    # There are 4 rows
    sum_ = 0
    for r in p:
        sum_ = sum_ + c[r][i]
    return sum_


if __name__ == "__main__":
    c = [
            [1, 2],
            [13, 4],
            [8, 16],
            [7, 3]
    ]
    m = max_sum_checkerboard_pebbles(c)
    print(m)

    c = [
            [1, 2, 9, 1],
            [13, 4, 0, 8],
            [8, 16, 24, 7],
            [7, 3, 8, 5]
    ]
    m = max_sum_checkerboard_pebbles(c)
    print(m)

