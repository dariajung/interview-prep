# write code to partition a linked list around a given value x
# such that nodes less than x come before x, and nodes greater than
# x come after x

# singly linked list?

import linkedlist

def partition(_list, x):
    # greater and less are "heads" of sub linked lists
    # which will be joined after all nodes are partitioned
    greater = None
    less = None
    current = _list.head
    equal = None
        
    while current != None:
        if current.value < x:
            if less == None:
                less = current
            else:
                less.next = current
                less = less.next
        elif current.value > x:
            if greater == None:
                greater = current
            else:
                greater.next = current
                greater = greater.next
        else:
            if equal == None:
                equal = current
            else:
                equal.next = current
                equal = less.next

        current = current.next

    greater.next = None

    if equal:
        less.next = equal
        equal.next = greater
    else:
        less.next = greater

if __name__ == "__main__":
    linked = linkedlist.LinkedList()

    for x in [1,4,9,3,2]:
        linked.push(x)

    partition(linked, 4)
    linked.traverse()