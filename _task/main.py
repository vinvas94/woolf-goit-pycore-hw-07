from _utils._parse_input import parse_input
from _contacts._contacts import *
from _functions._functions_contact import add_contact, change_contact, show_phone, show_all, delete_contact
from _functions._functions_birthday import add_birthday, show_birthday, birthdays
from _address_book._address_book import AddressBook


def main():
    book=AddressBook()
    print("Welcome to the assistant bot!😎")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?😊")
            elif command == "add":
                print(add_contact(args,book))
            elif command == "change":
                print(change_contact(args,book))
            elif command == "phone":
                print(show_phone(args[0], book))
            elif command == "all":
              print(show_all(book))
            elif command == "add-birthday":                
                print(add_birthday(args,book))
            elif command == "show-birthday":
                print(show_birthday(args,book))
            elif command == "birthdays":
               print (birthdays(book))
            elif command == "delete":
                print(delete_contact(args, book)) 
            else:
                print("Invalid command.😴")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")




if __name__ == "__main__":
    main()




