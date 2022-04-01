# Reverse a Linked List
'''
input: Head of following linked list 
1->2->3->4->NULL 
Output: Linked list should be changed to, 
4->3->2->1->NULL
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def ReverseLL(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def PrintList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.push(5)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)

    print("original linked list=")
    ll.PrintList()
    print("\nReversed linked list=")
    ll.ReverseLL()
    ll.PrintList()

