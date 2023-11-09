class BankAccount:
    __balance = 0  # hide it from other classes

    def __init__(self, balance):  # constructor -- initialize class data/variables
        self.__balance = balance

    def get_balance(self):  # other classes can see get balance
        return self.__balance

    def account_deposit(self, credit):
        if credit >= 0:
            self.__balance += credit
        else:
            print(f"Parameter not accepted.")

    def account_withdraw(self, debit):
        if debit >= 0:
            self.__balance -= debit
        else:
            print(f"Parameter not accepted.")
    


