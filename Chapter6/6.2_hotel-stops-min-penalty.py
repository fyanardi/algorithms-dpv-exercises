"""
6.2 You are going on a long trip. You start on the road at mile post 0. Along the way there are n
hotels, at mile posts a1 < a2 < ... < an, where each ai is measured from the starting point. The
only places you are allowed to stop are at these hotels, but you can choose which of the hotels you
stop at. You must stop at the final hotel (at distance an), which is your destination.

You'd ideally like to travel 200 miles a day, but this may not be possible (depending on the spacing
of the hotels). If you travel x miles during a day, the penalty for that day is (200 - x)^2. You
want to plan your trip so as to minimize the total penalty - that is, the sum, over all travel days,
of the daily penalties. Give an efficient algorithm that determines the optimal sequence of hotels
at which to stop
"""

import sys

"""
Return optimal sequence of hotels at which to stop and the minimum penalty corresponding to the
sequence
"""
def hotel_stops_min_penalty(a):
    # Let's define a0 = starting position = 0
    a_ = a[:]
    a_.insert(0, 0)
    P = [ 0 for x in a_ ]
    # Previous stop that minimizes the penalty at each mile stop
    s = [ 0 for x in a_ ]
    for i in range(1, len(a_), 1):
        P[i] = sys.maxsize # initialize to infinity
        for j in range(i):
            # If we don't care about the actual stops, we can just use min as below
            # P[i] = min(P[i], P[j] + (200 - (a[i] - a[j])) ** 2)

            # Keep track of the previous stop that minimizes penalty at mile post i
            p = P[j] + (200 - (a_[i] - a_[j])) ** 2
            if p < P[i]:
                s[i] = j
                P[i] = p

    stops = []
    k = i
    while k > 0:
        stops.append(k)
        k = s[k]

    return (P[i], stops[::-1])


if __name__ == "__main__":
    # Another implementation in Java: https://github.com/iamprem/algorithms/blob/master/Hotel.java
    a = [ 190, 420, 550, 660, 670 ]
    p, s = hotel_stops_min_penalty(a)
    print('Stops=[%s] Minimum penalty = %d sequence = %s' % (a, p, s))

    a = [ 10, 200, 270, 430, 500 ]
    p, s = hotel_stops_min_penalty(a)
    print('Stops=[%s] Minimum penalty = %d sequence = %s' % (a, p, s))

