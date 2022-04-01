#Topics =  

# 1)library management
# 2)cakeshop
# 3)parking slot allotment
# 4)vehical rental system
# 5)quiz application

# Library management=
'''
Book=->id,name,author,status

admin =>add new book,view all book,search book
        edit book,delete book

coustomer=>view all books,search books-id,name,author based (provide status available or not)
           issue book,submit book=1,10-9-2021(return date) after return book will be 1


2 files needed=>
file1=bankinfo
1,let us c,kanetkar,1(available) -->after issue 1 will be 0
2.learning python,vaishali,1

file2=
issuebook
data-1,1-9,2021,karan

if you return book in 7 days then ok and after that 3days fine
'''

# with open("text.txt","w") as fp:  #no need of close
#         fp.write("first\n")
#         fp.write("second\n")
data = "101,kk,2000"
x = "101"

# if(x in data):
#     print("found")
# else:
#     print("not")
print(data.index(x,0,3))