'''
Input:
LinkedList: 1->2->2->4->5->6->7->8
K = 4

Output: 4 2 2 1 8 7 6 5 
Explanation: 

The first 4 elements 1,2,2,4 are reversed first 
and then the next 4 elements 5,6,7,8. Hence, the 
resultant linked list is 4->2->2->1->8->7->6->5.
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
    
class LinkList:
    def __init__(self):
        self.head = None

    def reverse(self,head,k):
        if head==None:
            return None
        current = head
        next = None
        prev = None
        count = 0

        while(current is not None and count<k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        if(next is not None):
            head.next = self.reverse(next,k)
        return prev

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
    ll = LinkList()
    ll.push(9)
    ll.push(8)
    ll.push(7)
    ll.push(6)
    ll.push(5)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    
    print("original Linked list=")
    ll.PrintList()
    print("\nAfter Reverse Linked List=")
    ll.head = ll.reverse(ll.head,3)
    ll.PrintList()