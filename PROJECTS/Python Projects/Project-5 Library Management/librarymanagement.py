
class library:

    def __init__(self,listofbooks):
        self.books=listofbooks
    
    def displayAvailablebook(self):
        print("Books present in this library are: ")
        for book in self.books:
             print(" *" + book)
    

    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname}. Please keep it safe and return it within 30 days")
            self.books.remove(bookname)
            return True

        else:
            print("Sorry, This book is not available or has already been issued to someone else. Please wait until the book is available")
            return False
        

    def returnbook(self,bookname):
        self.books.append(bookname)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")



class student:

    def requestbook(self):
        self.book=input("Enter name of the book you want to borrow: ")
        return self.book

    def returnbook(self):
        self.book=input("Enter name of the book you want to return: ")
        return self.book


if __name__ == '__main__':
    
    Central_library= library(["Algorithms", "Django", "Clrs", "Python Notes","OpenCV"])
    student=student()
    
    while(True):

        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)

        a=int(input("Enter choice= "))
        if a==1:
            Central_library.displayAvailablebook()
        elif a==2:
            Central_library.borrowbook(student.requestbook())
        elif a==3:
            Central_library.returnbook(student.returnbook())
        elif a==4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("invalid choice!")