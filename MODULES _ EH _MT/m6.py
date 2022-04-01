
def f1():

    try:
        x = int(input("enter a number="))
        print("you entered:",x)
    
    except ValueError:
        print("number entered is invalid")
        raise 
    finally:  #compulsory run whether error occurs or not occurs
        print("-----i am end of program-----")

if __name__ == '__main__':
    f1()
    