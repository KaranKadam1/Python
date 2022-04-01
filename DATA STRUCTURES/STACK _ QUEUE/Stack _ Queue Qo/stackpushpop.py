# stack push pop using list

stack=[]
n=int(input("enter maxsize of stack= "))


def push():
    if len(stack)==n:
        print("stack is full !")
    else:
        item=int(input("enter items= "))
        stack.append(item)
        print(stack)

def pop():
    if not stack:
        print("stack is empty!")
    else:
        e = stack.pop()
        print("removed element= ",e)
        print(stack)


while True:
    print("select operation= 1.push 2.pop 3.quit")
    choice=int(input())
    
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("please enter correct choice!")
    