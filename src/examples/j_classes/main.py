import bank_account, atm, menu

account = bank_account.BankAccount(50)

# print(f"{my_account.get_balance()}")

# my_account.account_deposit(50)
# print(f"{my_account.get_balance()}")

# my_account.account_withdraw(50)
# print(f"{my_account.get_balance()}")

menu = menu.Menu()
menu.menu_run()