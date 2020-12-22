from datetime import datetime
from dateutil.relativedelta import relativedelta
from myprint import print_bar
from myprint import print_center, input_center

TABLE_NAME = "members"
MEMBERSHIP_PERIOD = 3


class Member:
    def __init__(self):
        self.member_id = 0
        self.name = ""
        self.address = ""
        self.phone = ""
        self.joining_date = ""
        self.valid_till = ""

    def create(self, member_id, name, address, phone, joining_date, valid_till):
        self.member_id = member_id
        self.name = name
        self.address = address
        self.phone = phone
        self.joining_date = joining_date
        self.valid_till = valid_till
        return self

    def create_from_record(self, record):
        self.member_id = record['id']
        self.name = record['name']
        self.address = record['address']
        self.phone = record['phone']
        self.joining_date = record['joining']
        self.valid_till = record['valid_till']
        return self

    def print_all(self):
        print(str(self.member_id).ljust(3),
              self.name[0:15].ljust(15),
              self.address[0:15].ljust(15),
              self.phone.ljust(15),
              self.joining_date.strftime("%d-%b-%y").ljust(15),
              (self.valid_till.strftime("%d %b %y") if self.valid_till is not None else "None").ljust(15))

    def print_full(self):
        print_bar()
        print("Member #", self.member_id)
        print("Name: ", self.name)
        print("Address: ", self.address)
        print("Phone: ", self.phone)
        print("Joined on ", self.joining_date.strftime("%d %b %y"))
        print("Membership expires on : ", self.valid_till.strftime("%d %b %y") if self.valid_till is not None else None)
        print_bar()


def create_member():
    member_id = None
    name = input_center("Enter the name: ")
    address = input_center("Enter the address: ")
    phone = input_center("Enter the phone: ")
    joining_date = datetime.now()
    valid_till = joining_date + relativedelta(months=MEMBERSHIP_PERIOD)
    return Member().create(member_id, name, address, phone, joining_date, valid_till)


def print_header():
    print("="*100)
    print("id".ljust(3),
          "name".ljust(15),
          "address".ljust(15),
          "phone".ljust(15),
          "joining".ljust(15),
          "expiry".ljust(15))
    print("="*100)


def create_members_table(database):
    cursor = database.cursor()
    cursor.execute("DROP table if exists {0}".format(TABLE_NAME))
    cursor.execute("create table {0} ("
                   "id int primary key auto_increment,"
                   "name varchar(20),"
                   "address varchar(50),"
                   "phone varchar(10),"
                   "joining datetime,"
                   "valid_till datetime)".format(TABLE_NAME))

