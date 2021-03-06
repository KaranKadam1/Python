# Deleting node in linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node= Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def DeleteNode(self,key):
        temp = self.head
        if(temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return

        while(temp is not None):
            if(temp.data == key):
                break
            prev = temp
            temp = temp.next

        if(temp == None):
            return
        prev.next = temp.next
        temp = None

    def Printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    
    ll = LinkedList()
    ll.push(7)
    ll.push(1)
    ll.push(3)
    ll.push(2)

    print("Created linked list=")
    ll.Printlist()
    
    ll.DeleteNode(1)
    print("Linked list after deletion of 1=")
    ll.Printlist()

