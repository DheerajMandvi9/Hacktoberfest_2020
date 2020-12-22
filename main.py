import sys
from books import book_menu
from issue_returns import issue_return_menu
from members import member_menu
from myprint import print_center, input_center
from database import get_database
if __name__ == '__main__':
    database, cursor = get_database()
    if database is None:
        print("The Database does not exist or not accessible.")
        sys.exit(1)
    while True:
        print()
        print_center("==============================")
        print_center("============Library===========")
        print_center("==============================")
        print_center("1. Manage Members")
        print_center("2. Issue/Return Register")
        print_center("3. Manage Books")
        print_center("0. Exit")
        print()
        choice = int(input_center("Enter your choice: "))
        if choice == 2:
            issue_return_menu(database,cursor)
        elif choice == 3:
            book_menu(database, cursor)
        elif choice == 1:
            member_menu(database, cursor)
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to exit)")
    print_center("GoodBye")