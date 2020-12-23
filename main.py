import sys
from books import book_menu
from issue_returns import issue_return_menu
from members import member_menu
from myprint import print_center, input_center
from database import get_database
import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
if __name__ == '__main__':
    database, cursor = get_database()
    if database is None:
        print("The Database does not exist or not accessible.")
        sys.exit(1)
    while True:
        print()
        print_center(Fore.RED+"==============================")
        print_center(Fore.RED+"============Library===========")
        print_center(Fore.RED+"==============================")
        print_center(Fore.YELLOW+"1. Manage Members")
        print_center(Fore.YELLOW+"2. Issue/Return Register")
        print_center(Fore.YELLOW+"3. Manage Books")
        print_center(Fore.YELLOW+"0. Exit")
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