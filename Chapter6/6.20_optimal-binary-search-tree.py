"""
6.20 Optimal binary search trees. Suppose we know the frequency with which keywords occur in program
of a certain language, for instance:

    begin   5%
    do      40%
    else    8%
    end     4%
    if      10%
    then    10%
    while   23%

We want to organize them in a binary search tree, so that the keyword in the root is alphabetically
bigger than all the keywords in the left subtree and smaller than all the keywords in the right
subtree (and this holds for all nodes).

Figure 6.12 has a nicely-balanced example on the left. In this case, when a keyword is being looked
up, the number of comparison needed is at most three: for instance, in finding "while", only the
three nodes "end", "then", and "while" get examined. But since we know the frequency with which
keywords are accessed, we can use an even more fine-tuned cost function, the average number of
comparisons to look up a word. For the search tree on the left, it is:

    cost = 1(0.04) + 2(0.40 + 0.10) + 3(0.05 + 0.08 + 0.10 + 0.23) = 2.42

By this measure, the best search tree is the one on the right, which has a cost of 2.18.

Give an efficient algorithm for the following task.
    Input: n words (in sorted order); frequencies of these words: p_1, p_2, ..., p_n.
    Output: The binary search tree of lowest cost (defined above as the expected number of
    comparisons in looking up a word).
"""

import sys

def optimal_binary_search_tree(p):
    """
    Returns the lowest cost among all possible binary search trees.
    Args:
        p: array of words frequencies
    """
    T = [[ 0 for i in p] for j in p]
    n = len(p)

    for s in range(n):
        for i in range(n - s):
            j = i + s
            if i == j:
                T[i][j] = p[i]
                continue

            T[i][j] = sys.maxsize

            for k in range(i, j+1):
                T_L = T[i][k-1] if k > i else 0
                T_R = T[k+1][j] if k < j else 0
                T[i][j] = min(T[i][j], T_L + T_R)

            for k in range(i, j+1):
                T[i][j] = T[i][j] + p[k]

    return T[0][n-1]


if __name__ == "__main__":
    # test case from exercise 6.20
    p = [ 0.05, 0.4, 0.08, 0.04, 0.10, 0.10, 0.23 ]
    c = optimal_binary_search_tree(p)
    print('p=%s c=%s' % (p, c))

    # test case from https://www.geeksforgeeks.org/optimal-binary-search-tree-dp-24/
    p = [ 34, 8, 50 ]
    c = optimal_binary_search_tree(p)
    print('p=%s c=%s' % (p, c))

