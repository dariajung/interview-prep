
def merge(a, b):

    if not a and b:
        return b

    if not b and a:
        return a

    if a and b:
        ha = a.pop(0)
        hb = b.pop(0)
        if ha <= hb:
            return [ha] + merge(a, [hb] + b)
        elif ha > hb:
            return [hb] + merge([ha] + a, b)

def mergesort(arr):
    if not arr:
        return []

    elif len(arr) == 1:
        return arr

    else:
        pivot = len(arr) / 2
        lesser = arr[:pivot]
        greater = arr[pivot:len(arr)]
        return merge(mergesort(lesser), mergesort(greater))

if __name__ == "__main__":
    print mergesort([3, 6, 1, 60, 13, 42, 521, 42, -1, 0])
