import atm, bank_account

class Menu:
    account = bank_account.BankAccount(100)

    def __init__(self):
        pass

    def menu_display(self):
        print(f"COSC Bank")
        print(f"1 - Deposit")
        print(f"2 - Withdraw")
        print(f"3 - Balance")
        print(f"4 - Exit")

    def menu_run(self):
        menu = Menu()
        menu.menu_display()
        selection = input(f"Please make a selection from the above menu: ")
        program_run = atm.ATM(self.account)
        if selection == '1':
            program_run.make_deposit()
            menu.menu_run()
        elif selection == '2':
            program_run.make_withdraw()
            menu.menu_run()
        elif selection == '3':
            program_run.display_balance()
            menu.menu_run()
        elif selection == '4':
            exit()
        else:
            print(f"Please make a valid selection.")
            menu.menu_run()

    
