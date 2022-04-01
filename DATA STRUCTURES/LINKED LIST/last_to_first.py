# Move last element to front of a given Linked List
'''
Write a function that moves the last element to the front in a given Singly Linked List.
For example, if the given Linked List is 1->2->3->4->5,
then the function should change the list to 5->1->2->3->4.
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def MoveLastToFront(self):
        temp = self.head
        sec_last = None

        if not temp and temp.next:
            return
        while temp and temp.next:
            sec_last = temp
            temp = temp.next
        sec_last.next = None
        temp.next = self.head
        self.head = temp
        
    def push(self,new_data): 
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def PrintList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp= temp.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.push(5)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)

    print("Original Linked List=")
    ll.PrintList()
    print("\nAfter Moving=")
    ll.MoveLastToFront()
    ll.PrintList()