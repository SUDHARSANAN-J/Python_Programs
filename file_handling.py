def store_data():
    print()
    Book_Name = input("Enter the Book Name : ")
    Book_Author = input("Enter the Book Author : ")
    Publisher = input("Enter the Publisher : ")
    Book_year = int(input("Enter the Book Year : "))
    Book_Details = ["Book Name : " +Book_Name,"\n", "Book Author : " +Book_Author,"\n", "Publisher : " +Publisher,"\n", "Book Year : " +str(Book_year),"\n"]
    details = open("library.txt","a")
    details.writelines(Book_Details)
    details.write("\n")
    details.close()
    print()
    print("*"*40,"Book Details stored","*"*40)
    print()
def Retrieve_Book():
    print("\nAvailable Books in the library\n")
    Availability = open("library.txt","r")
    print(Availability.read())
    Availability.close()
    print("*"*40,"These are the available books in the library","*"*40)
    print()
def Delete_all_details():
    Deleting = open("library.txt","w")
    Deleting.close()
    print()
    print("*"*40,"Deleted all the books in the library","*"*40)
    print()

while True:
    print("1. Store a new Book details")
    print("2. Retrieve the available Book details")
    print("3. Delete the book details")
    print("4. Exit\n")
    choice = int(input("Enter the operation to be performed (1/2/3/4) : "))

    if choice == 1:
        store_data()
    elif choice == 2:
        Retrieve_Book()
    elif choice == 3:
        Delete_all_details()
    else:
        print()
        print("*"*40,"Exiting Program","*"*40)
        break

