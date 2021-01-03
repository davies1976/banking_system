import random
import math
import sqlite3

accounts = []


class BankingDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS card (
                                           id integer PRIMARY KEY,
                                           number text NOT NULL,
                                           pin text NOT NULL, 
                                           balance integer DEFAULT 0
                                       );"""
        self.cur.execute(sql_create_tasks_table)
        self.conn.commit()

    def write_card(self, number, pin, balance):
        sqlite_insert_query = f"""INSERT INTO card
                              (number, pin, balance) 
                               VALUES 
                              ({number},{pin},{balance})"""

        self.cur.execute(sqlite_insert_query)
        self.conn.commit()

    def read_card(self):
        pass


class Card:
    def __init__(self):
        self.iin = 400000
        self.account_number = random.randint(1, 999999999)
        self.new_card_number()
        self.checksum = 0
        self.pin_number = str(random.randint(0, 9999)).zfill(4)
        self.cardnumber = str(self.iin) + str(self.account_number).zfill(9)
        self.create_checksum()
        self.cardnumber += str(self.checksum)
        self.balance = 0
        account_db = BankingDatabase()
        account_db.create_table()
        account_db.write_card(self.cardnumber, self.pin_number, self.balance)
        accounts.append(
         {"cardnumber": self.cardnumber,
             "pinnumber": self.pin_number,
             "Balance": self.balance}
        )

    def new_card_number(self):
        while self.account_number in accounts:
            self.account_number = random.randint(1, 999999999)
            self.checksum = 0

    def create_checksum(self):
        transformed_number = []
        digit_count = 1
        checksum_value = 0
        for digit in self.cardnumber:
            int_digit = int(digit)
            if digit_count % 2:
                int_digit = int_digit * 2
                if int_digit > 9:
                    int_digit = int_digit - 9
                    transformed_number.append(int_digit)
                else:
                    transformed_number.append(int_digit)
            else:
                transformed_number.append(int_digit)
            checksum_value = checksum_value + int_digit
            digit_count += 1
        rounded = math.ceil(checksum_value / 10) * 10
        self.checksum = rounded - checksum_value


menu_running = True

while menu_running:
    option = int(input(
        "1. Create an account\n2. Log into account\n0. Exit\n>"))

    if option == 1:
        print("Your card has been created")
        new_card = Card()
        print(f"Your card number is:\n{new_card.cardnumber}")
        print(f"Your card PIN:\n{new_card.pin_number}")
    elif option == 2:
        card_number = input("Enter your card number:\n>")
        pin_number = input("Enter your PIN:\n>")
        for card in accounts:
            if card_number == card["cardnumber"] and pin_number == card["pinnumber"]:
                print("You have successfully logged in!\n\n")
                user_menu = True
                while user_menu:
                    user_action = int(input("1. Balance\n2. Log Out\n0. Exit\n>"))
                    if user_action == 1:
                        print(f"Balance: {card['Balance']}")
                    elif user_action == 2:
                        user_menu = False
                    elif user_action == 0:
                        user_menu = False
                        menu_running = False
            else:
                print("Wrong card number or PIN!")
                break
    elif option == 0:
        menu_running = False

print("\nBye!")
