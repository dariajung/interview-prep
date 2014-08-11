# Given a list of numbers in random order write a 
# linear time algorithm to find the kth smallest 
# number in the list. Explain why your algorithm is linear.

def k_smallest(_list, k):
    d = dict()
    for i in _list:
        d[i] = "whatever"

    for i, v in enumerate(d):
        if k > len(d):
            return None

        if i == (k - 1):
            return v

if __name__ == "__main__":
    test = [7, 4, 8, 11, 2, 5]
    print k_smallest(test, 10)