from datetime import datetime
from myprint import print_center, input_center

from myprint import print_bar

TABLE_NAME = "issue_return"


class IssueReturn:
    def __init__(self):
        self.record_id = 0
        self.book_id = ""
        self.book_title = ""
        self.member_id = ""
        self.member_name = ""
        self.issue_date = ""
        self.return_date = ""

    def create(self, record_id, book_id, book_title, member_id, member_name, issue_date, return_date):
        self.record_id = record_id
        self.book_id = book_id
        self.book_title = book_title
        self.member_id = member_id
        self.member_name = member_name
        self.issue_date = issue_date
        self.return_date = return_date
        return self

    def create_from_record(self, record):
        self.record_id = record['id']
        self.book_id = record['book_id']
        self.book_title = record['book_title']
        self.member_id = record['member_id']
        self.member_name = record['member_name']
        self.issue_date = record['issue_date']
        self.return_date = record['return_date']
        return self

    def print_all(self):
        print(str(self.record_id).ljust(3),
              str(self.book_id).ljust(15),
              self.book_title[0:15].ljust(15),
              str(self.member_id).ljust(15),
              self.member_name[0:15].ljust(15),
              self.issue_date.strftime("%d-%b-%y").ljust(15),
              (self.return_date.strftime("%d %b %y") if self.return_date is not None else "None").ljust(15))

    def print_full(self):
        print_bar()
        print("Record #", self.record_id)
        print("Book id: ", self.book_id)
        print("Book Title: ", self.book_title)
        print("Member id: ", self.member_id)
        print("Member Name: ",self.member_name)
        print("Issue Date: ", self.issue_date.strftime("%d %b %y"))
        print("Return date: ", self.return_date.strftime("%d %b %y") if self.return_date is not None else None)
        print_bar()


def create_record(book, member):
    record_id = None
    issue_date = datetime.now()
    return_date = None
    return IssueReturn().create(record_id,book.book_id, book.title, member.member_id, member.name, issue_date, return_date)


def print_header():
    print("="*100)
    print("id".ljust(3),
          "bookid".ljust(15),
          "book title".ljust(15),
          "member id".ljust(15),
          "member name".ljust(15),
          "issue date".ljust(15),
          "return date".ljust(15))
    print("="*100)


def create_issue_return_table(database):
    cursor = database.cursor()
    cursor.execute("DROP table if exists {0}".format(TABLE_NAME))
    cursor.execute("create table {0} ("
                   "id int primary key auto_increment,"
                   "book_id int,"
                   "book_title varchar(50),"
                   "member_id int,"
                   "member_name varchar(50),"
                   "issue_date datetime,"
                   "return_date datetime)".format(TABLE_NAME))

