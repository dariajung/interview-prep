import linkedlist

def remove_duplicates(_list):
    current = _list.head
    runner = _list.head.next
    runner_prev = _list.head

    while current != None:
        #print current.value
        while runner != None:
            if runner.value == current.value:
                runner_next = runner.next
                runner_prev.next = runner_next
                # runner_prev stays the same
                runner = runner_next
            else:
                runner_prev = runner
                runner = runner.next

        current = current.next

        if current == None:
            break
        else:
            runner = current.next
            runner_prev = current


if __name__ == "__main__":
    linked = linkedlist.LinkedList()

    for i in "follow up":
        linked.push(i)

    remove_duplicates(linked)

    linked.traverse()