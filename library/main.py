"""this is the main module contain many information"""

from accounts import LibrarianAccount, MemberAccount

def menu():
    while True:
        print("*"*30,
              "\nWelcome to the library of the wizards\n"
              "How do you want to login \n"
              "1) Librarian\n"
              "2) Student\n"
              "3) Create Account")
        choice = int(input("Select one number from the above : "))

        if choice == 1:
            _librarian_login()
            break
        elif choice == 2:
            _member_login()
            break
        elif choice == 3:
            _create_account()
            break
        else:
            print("Wrong choice please select again\n")


def _librarian_login():
    librarina_id = input("Please enter your Librarian ID : ")
    password = input("Please enter your password ")


    # if match records
    # else
def _member_login():
    pass

def _create_account():
    while True:
        acc_choice = input("1) Librarian \n"
                           "2) Member Account")

        if acc_choice == 1:
            pass
        elif acc_choice == 2:
            pass
        else:
            print("wrong entry try again\n")