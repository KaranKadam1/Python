from book import Book
from bookMgmt import BookMgmt

def user():
    bookMgmt = BookMgmt()
    choice = 0

    while (choice != 7):
        print("<<<<<<---Choose From Following As per Your Requirement--->>>>>>\n")
        print('''\t\t\t1.View All Book
                 \t2.Search Book By Id
                 \t3.Search Book By Name
                 \t4.Search Book By Author
                 \t5.Issue Book 
                 \t6.Submit Book 
                 \t7.Exit \n''')

        choice = int(input("Enter your choice = "))

        if (choice == 1):
            print("\n-----Available Books Are-----\n")
            bookMgmt.showAllBooks()

        elif (choice == 2):
            id = int(input("Enter the book id = "))
            bookMgmt.searchBookById(id)

        elif (choice == 3):
            name = input("Enter book Name = ")
            bookMgmt.searchBookByName(name)

        elif (choice == 4):
            author = input("Enter book author name = ")
            bookMgmt.searchBookByAuthor(author)

        elif (choice == 5):
            id = int(input("Enter the book id which you want to issue = "))
            bookMgmt.issueBook(id)

        elif(choice == 6):
            id = int(input("Enter the book id which you want to submit = "))
            bookMgmt.SubmitBook(id)
        
        elif(choice==7):
            print("Thank you for visiting..Have a Good Day = ")

if(__name__ == "__main__"):
    user()
