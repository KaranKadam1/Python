# program to introduce linked list

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

if __name__ == '__main__':
    
    ll = LinkedList()

    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    ll.head.next = second;
    second.next = third;

    