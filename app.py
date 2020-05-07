from utils import database

USER_CHOICE = """
Enter: 
- 'a' to add
- 'l' to list
- 'r' to mark
- 'd' to delete
- 'q' to quit
"""


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q:':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown input value. Please try again")

        user_input = input(USER_CHOICE)


def prompt_add_book(name, author):
    name = input("enter name of the book: ")
    author = input("enter name of the author: ")

    database.add_book(name, author)


def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'Yes' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_read_book():
    name = input("Enter the name of the book read: ")

    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input('Enter the book you want to delete: ')

    database.(name)


menu()