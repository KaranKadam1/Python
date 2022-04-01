# MAIN METHOD=

'''
__name__ = __main__
'''
def display():
    print(__name__)
# display()

'''
for ignore unwantedpart in another file when we accesing main file:
    we just put that info into if(__name__=="__main__"):
    it will hide the content in in next file ...so we dont need to comment unwanted data.
'''

# Exception Handling=
'''
Errors = syntax error = detected by editor
         logical error = concept mistake

Exception = unwanted error or situation in a program that causes abrupt termination of program.
Exception Handling = if code get errors then our program sent some msg rather than crash .
handling the error/exception and not letting program to crash.(defencive-programming)

keyword=try,except,raise,else,finally

error which reaches to os called unhandled exception

generalized exception handler handles all types of exceptions
'''
# try:
#     x = int(input("enter num="))
# except:
#     # this will execute when there is error
#     print("you have not entered a valid num")
# else:
#     # this will execute when there is no error
#     print("you entered:",x)



result = 0
try:
    num1 = int(input("enter num1="))  #value error can occur
    num2 = int(input("enter num2="))
    result = (num1/num2)  #zero division  error can occur when num is 0
    fp = open("text.txt","r")  #file not found

except ValueError:
    # this will execute when there is error
    print("you have not entered a valid num")

except ZeroDivisionError:
    print("second number not be 0")

except:  #if any error missed then thid handles remaining error
    print("something went wrong")

else:
    # this will execute when there is no error
    print("Result=:",result)

# except = generalized
# except valueerror = specialized e h
