# insertion node methods of linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):  #push node at begining
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertafter(self,prev_node,new_data):  #insert after any node

        if prev_node is None:
            print("previous node must be in linkedlist")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self,new_data):  #add node at last
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next

if __name__ == '__main__':
    ll = LinkedList()

    ll.append(6)
    ll.push(7)
    ll.push(1)
    ll.append(4)
    ll.insertafter(ll.head.next, 8)

    ll.printlist()
    
    



