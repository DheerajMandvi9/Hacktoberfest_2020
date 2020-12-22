from datetime import datetime
from myprint import print_center, input_center
import mysql
from issue_return import create_record, TABLE_NAME, create_issue_return_table, print_header,IssueReturn
from books import get_and_print_book_by_id, change_book_status
from members import get_and_print_member_by_id
NUMBER_OF_RECORDS_PER_PAGE = 10
BOOK_ISSUE_PERIOD = 30  # DAYS
LATE_FINE_PER_DAY = 1 # Rupees


def add_record(database, cursor):
    book = get_and_print_book_by_id(cursor)
    if book is not None:
        if not book.available:
            print("The Book Is Not Available")
            return
        member = get_and_print_member_by_id(cursor)
        if member is not None:
            record = create_record(book,member)
            confirm = input("Complete the operation? (Y/N) ").lower()
            if confirm == 'y':
                query = "insert into {0}(book_id, book_title,member_id, member_name,issue_date) " \
                        "values ({1},'{2}',{3},'{4}','{5}')".\
                    format(TABLE_NAME,record.book_id,record.book_title,record.member_id,
                           record.member_name,record.issue_date.strftime("%Y-%m-%d %H:%M:%S"))
                try:
                    cursor.execute(query)
                    database.commit()
                except mysql.connector.Error as err:
                    create_issue_return_table(database)
                    cursor.execute(query)
                    database.commit()
                change_book_status(database,cursor,book.book_id,False)
                print("Operation Successful")


def show_record(cursor, query):
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        if cursor.rowcount == 0:
            print("No Matching Records")
            return
        record = records[0]
        issue_record = IssueReturn().create_from_record(record)
        issue_record.print_full()
        return issue_record
    except mysql.connector.Error as err:
        print(err)


def show_records(cursor, query):
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        if cursor.rowcount == 0:
            print("No Matching Records")
            return
        print_header()
        for record in records:
            issue_record = IssueReturn().create_from_record(record)
            issue_record.print_all()
        return records
    except mysql.connector.Error as err:
        print(err)


def get_and_print_record_by_book_id(cursor):
    book_id = input("Enter the book id: ")
    query = "select * from {0} where book_id = {1} order by issue_date desc limit 1".format(TABLE_NAME, book_id)
    issue_record = show_record(cursor, query)
    return issue_record


def return_book(database, cursor):
    issue_record = get_and_print_record_by_book_id(cursor)
    if issue_record is not None:
        late_delta = datetime.now() - issue_record.issue_date
        if late_delta.days > BOOK_ISSUE_PERIOD:
            print("Calculated Fine: ", late_delta.days * LATE_FINE_PER_DAY , " Rupees")
        confirm = input("Complete the operation? (Y/N) ").lower()
        if confirm == 'y':
            return_date = datetime.now()
            query = "update {0} set return_date='{1}' where id={2}".\
                format(TABLE_NAME,return_date.strftime("%Y-%m-%d %H:%M:%S"),issue_record.record_id)
            cursor.execute(query)
            database.commit()
            change_book_status(database,cursor,issue_record.book_id,True)


def delete_record_by_book_id(database, cursor):
    issue_record = get_and_print_record_by_book_id(cursor)
    if issue_record is not None:
        confirm = input("Complete the operation? (Y/N) ").lower()
        if confirm == 'y':
            query = "delete from {0} where id={1}".format(TABLE_NAME,issue_record.record_id)
            cursor.execute(query)
            database.commit()
            print("Operation Successful")


def issue_return_menu(database, cursor):
    while True:
        print()
        print()
        print_center("============================")
        print_center("======Issue/Return Menu=====")
        print_center("============================")
        print()

        print_center("1. Issue A Book")
        print_center("2. Show Issue Record By Book ID")
        print_center("3. Return A Book")
        print_center("4. Show Books Issued By A Member")
        print_center("5. Show Books Whose Return Date has Passed")
        print_center("6. Delete Record")
        print_center("7. View all Records")
        print_center("0. Go Back")
        choice = int(input_center("Enter your choice: "))
        if choice == 1:
            add_record(database, cursor)
        elif choice == 2:
            get_and_print_record_by_book_id(cursor)
        elif choice == 3:
            return_book(database,cursor)
        elif choice == 4:
            member_id = int(input("Enter the member id: "))
            query = "select * from {0} where member_id={1} order by issue_date desc".format(TABLE_NAME, member_id)
            show_records(cursor, query)
        elif choice == 5:
            present_date = datetime.now()
            query = "select * from {0} where date_add(issue_date, INTERVAL {1} DAY) < '{1}'".\
                format(TABLE_NAME,BOOK_ISSUE_PERIOD,present_date.strftime("%Y-%m-%d"))
            show_records(cursor, query)
        elif choice == 6:
            delete_record_by_book_id(database, cursor)
        elif choice == 7:
            query = "select * from {0}".format(TABLE_NAME)
            show_records(cursor, query)
        elif choice == 0:
            break
        else:
            print_center("Invalid choice (Press 0 to go back)")