# We are given two sorted arrays A and B with n (positive or negative) integers each,
# and wish to determine if there is an element a of A and an element b of B such that a+b=100.
# Give an algorithm for this problem that runs in linear time (i.e. O(n) time) in the worst case.

import random


def sum_100(a, b):
    b_dict = dict()

    for x in b:
        b_dict[x] = None

    found = False

    for x in a:
        key = 100 - x
        if key in b_dict:
            found = True
            print x, key
            break

    return found


if __name__ == __main__:
    a = []
    b = []

    for x in xrange(100):
        a.append(random.randint(0, 100))

    for x in xrange(100):
        b.append(random.randint(0, 100))

    print sum_100(a, b)

