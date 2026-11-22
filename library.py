
# Library Management System

books = []

def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "name": book_name,
        "author": author,
        "available": True
    }

    books.append(book)
    print("Book added successfully!")


def display_books():
    if len(books) == 0:
        print("No books available.")
    else:
        print("\n--- Library Books ---")

        for book in books:
            print("Book ID:", book["id"])
            print("Book Name:", book["name"])
            print("Author:", book["author"])

            if book["available"]:
                print("Status: Available")
            else:
                print("Status: Issued")

            print("-------------------")


def search_book():
    book_id = input("Enter Book ID to search: ")

    for book in books:
        if book["id"] == book_id:
            print("Book Found!")
            print("Book Name:", book["name"])
            print("Author:", book["author"])
            return

    print("Book not found.")


def issue_book():
    book_id = input("Enter Book ID to issue: ")

    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                print("Book issued successfully!")
            else:
                print("Book is already issued.")
            return

    print("Book not found.")


def return_book():
    book_id = input("Enter Book ID to return: ")

    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                book["available"] = True
                print("Book returned successfully!")
            else:
                print("Book was not issued.")
            return

    print("Book not found.")


def main():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Thank you for using Library Management System!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()