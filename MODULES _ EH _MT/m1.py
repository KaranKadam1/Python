# Modules = Any Python File termed as an module eg(test.py = module->test)

'''
ways to access func or method using another module =

1)import myfunction = 
myfaction.fact()

if we have to file and we have to acces these file methods with another file=
eg --> s = myCode.student(101,"karan")  here my
       print("factorial=",myCode.fact(4))


2) import myCode as c  --->here c is alias name(nick name)


3)from myCode import student,fact
  from myCode import* (*=all)

'''

# Packages = folder which content python files(init.py)..first we create package folder then we create files inside
# it or we can just drag and drop the file
'''
import package1.test as t (package name.module name)

print("sum = ",t.sum(20,40))
t.fibo(10)

'''







