
import string
import random

if __name__ == '__main__':
    
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation

    password_len=int(input("Please Enter Password Lenght= \n"))
    s=[]
    s.extend(list(s1))
    s.extend(list(s1))
    s.extend(list(s1))
    s.extend(list(s1))
    

    print("Your Password is= ")
    print("".join(random.sample(s,password_len)))
 