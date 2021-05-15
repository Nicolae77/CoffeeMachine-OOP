class MoneyMachine:

    CURRENCY = "£"

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_money(self):
        """Returns the total calculated."""
        print("Please insert your money.")
        self.money_received = int(input(f"The machine accepts only £?: "))
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_money()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Take your {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False