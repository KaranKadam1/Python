def f1():
    try:
        x = int(input("enter a number from user="))
    except ValueError:
        print("child handler:please enter a valid number")#inner
        raise #re-throw the exception to main
    else:
        print("you entered: ",x)


if __name__ == '__main__':
    try:
        f1()
    except ValueError:
        print("main handler:entered no.is invalid")#outer
