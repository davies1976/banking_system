import random

accounts = []


class Card:
    def __init__(self):
        self.iin = 400000
        self.account_number = random.randint(1, 999999999)
        self.checksum = 0
        self.new_card_number()
        self.pin_number = random.randint(0, 9999)
        self.cardnumber = str(self.iin) + str(self.account_number) + str(self.checksum)
        self.balance = 0
        accounts.append(
         {"cardnumber": self.cardnumber,
             "pinnumber": str(self.pin_number).zfill(4),
             "Balance": self.balance}
        )

    def new_card_number(self):
        while self.account_number in accounts:
            self.account_number = random.randint(1, 999999999)
            self.checksum = 0


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
