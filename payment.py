class Payment:

    def __init__(self,amount):
        self.amount = amount

    def pay_cash(self):
        print(f"Paid $ {self.amount} in cash successfully!")

    def pay_card(self, card_number):
        if len(card_number) == 16 and card_number.isdigit():
            print(f"Paid $ {self.amount} using card ending with {card_number[-4:]} successfully!")
        else:
            print("Invalid Card Details. Payment Failed!")

            


