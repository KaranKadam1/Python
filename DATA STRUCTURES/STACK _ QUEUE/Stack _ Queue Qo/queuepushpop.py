 
queue=[]

def enqueue():
    item = int(input("enter items= "))
    queue.append(item)
    print(item, "is added to the queue")

def dequeue():
    if not queue:
        print("queue is empty!")
    else:
        e = queue.pop(0)
        print("removed item= ",e)

def display():
    print(queue)

while True:
    print("Enter the operation=\n 1.push 2.pop 3.show 4.quit")
    choice = int(input())

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("please enter the correct option!")
    