from myprint import print_bar
from myprint import print_center, input_center


TABLE_NAME = "books"


class Book:
    def __init__(self):
        self.book_id = 0
        self.title = 0
        self.author = ""
        self.topic = ""
        self.available = True

    def create(self, book_id, title, author, topic, available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.topic = topic
        self.available = available
        return self

    def create_from_record(self, record):
        self.book_id = record['id']
        self.title = record['title']
        self.author = record['author']
        self.topic = record['topic']
        self.available = record['available']
        return self

    def print_all(self):
        print(str(self.book_id).ljust(3),
              self.title.ljust(15),
              self.author.ljust(15),
              self.topic.ljust(15),
              ("YES" if self.available else "NO").ljust(15))

    def print_full(self):
        print_bar()
        print("Record #", self.book_id)
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Topic: ", self.topic)
        print("available: ", "YES" if self.available else "NO")
        print_bar()


def create_book():
    book_id = None
    title = input_center("Enter the title: ")
    author = input_center("Enter the author name: ")
    topic = input_center("Enter the topic: ")
    available = True
    return Book().create(book_id, title, author, topic, available)


def print_header():
    print("="*100)
    print("id".ljust(3),
          "Title".ljust(15),
          "Author".ljust(15),
          "Topic".ljust(15),
          "Available".ljust(15)
          )
    print("="*100)


def create_book_table(database):
    cursor = database.cursor()
    cursor.execute("DROP table if exists {0}".format(TABLE_NAME))
    cursor.execute("create table {0} ("
                   "id int primary key auto_increment,"
                   "title varchar(50),"
                   "author varchar(50),"
                   "topic varchar(50),"
                   "available bool)".format(TABLE_NAME))