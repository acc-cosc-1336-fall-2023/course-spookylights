

class ATM:
    __bank_account = None

    def __init__(self, bank_account):
        self.__bank_account = bank_account
        

    def display_balance(self):
        print(f"Your balance is {self.__bank_account.get_balance()}")

    def make_deposit(self):
        amount = int(input("Enter deposit amount: "))
        self.__bank_account.account_deposit(amount)
    
    def make_withdraw(self):
        amount = int(input("Enter withdraw amount: "))
        self.__bank_account.account_withdraw(amount)