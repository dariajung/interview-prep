
def quicksort(arr):
    if not arr:
        return arr
    else:
        pivot = arr.pop(0)

    lesser = [x for x in arr if x <= pivot]
    greater = [x for x in arr if x > pivot]

    return quicksort(lesser) + [pivot] + quicksort(greater)

if __name__ == "__main__":
    arr = [3, 6, 1, 60, 13, 42, 521, 42, -1, 0]
    print quicksort(arr)