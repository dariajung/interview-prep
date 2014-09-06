
class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

# Singly linked list
class LinkedList():

    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def traverse(self):
        current = self.head
        while current != None:
            print current.value
            current = current.next

    def reverse(self):
        current = self.head
        prev = None
        temp = self.head

        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        self.head = prev


if __name__ == "__main__":
    _list = LinkedList()
    
    for i in range(10):
        _list.push(i)

    _list.traverse()

    _list.reverse()
