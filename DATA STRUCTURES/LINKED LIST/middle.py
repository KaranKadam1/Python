# find the middle of given linked list
# '''
# Given a singly linked list, find the middle of the linked list. For example,
# if the given linked list is 1->2->3->4->5 then the output should be 3. 
# If there are even nodes, then there would be two middle nodes, we need to 
# print the second middle element. For example, 
# if given linked list is 1->2->3->4->5->6 then the output should be 4. 
# '''

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def PrintList(self):
        node = self.head
        while node:
            print(str(node.data) + "->" ,end=" ")
            node = node.next
        print("NULL")

    def PrintMiddle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Middle element is=",slow.data) 


if __name__ == '__main__':
    
    ll = LinkedList()

    for i in range(5,0,-1):
        ll.push(i)
        ll.PrintList()
        ll.PrintMiddle()
    # ll.push(5)
    # ll.push(4)
    # ll.push(1)
    # ll.PrintList()
    # ll.PrintMiddle()







