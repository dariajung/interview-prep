# implement an algorithm to find the kth to last element in a linked list

import random
import linkedlist

def kth_to_last(_list, k):
    _list.reverse()

    current = _list.head
    counter = 1

    while counter < k:
        current = current.next
        counter += 1

    return current.value 

if __name__ == "__main__":
    linked = linkedlist.LinkedList()

    for i in range(20):
        linked.push(random.randint(0, 10))

    linked.traverse()
    print ("\n------------")

    print kth_to_last(linked, 3)
