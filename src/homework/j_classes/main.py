import class_a


class Menu:

    def menu_display(self):
        print(f"""
              +------------------------+
              |   Dice Roll Simulator  |
              |  ~*~*~*~*~*~*~*~*~*~*~ |
              +------------------------+
              """)

    def menu_run(self):

        self.menu_display()
        selection = input(f"1 to roll the die, any other key to exit: ")
        die_roll = class_a.Die()
        while selection == '1':
            print(die_roll)
            selection = input(f"1 to roll the die, any other key to exit: ")


die_sim_start = Menu()
die_sim_start.menu_run()
