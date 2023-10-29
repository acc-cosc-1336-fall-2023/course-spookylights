import dictionary, pprint

def display_menu():
    print("1 - Add or Update Item")
    print("2 - Delete Item")
    print("3 - Exit")

def program_selection():
    display_menu()
    opt = input("Please make a selection from the menu: ")
    if opt == '1':
        run_add_inventory()
    elif opt == '2':
        run_del_item()
    elif opt == '3':
        print("Goodbye!")
        exit()
    else:
        print('Must choose a valid selection from the menu. Restarting.')
        program_selection()

def run_add_inventory():
    widget_name = input('Please enter the name of the item you are adding: ')
    quantity = int(input("Please enter the quantityof this item: "))
    dictionary.add_inventory(widget_name,quantity)

    print("The current inventory is: ")
    pprint.pprint(dictionary.widget_inv)
    print('----------------------------------------')
    print('Add or update the inventory again?')
    cont = input('1 to continue, any other key to return to the main menu: ')
    if cont == '1':
        run_add_inventory()
    else:
        program_selection()

def run_del_item():
    widget_name = input("Input record to remove: ")
    dictionary.remove_inventory_widget(widget_name)

    print('The current inventory is: ')
    pprint.pprint(dictionary.widget_inv)
    print('----------------------------------------')
    print('Remove another item?')
    cont = input('1 to continue, any other key to return to the main menu: ')
    if cont == '1':
        run_del_item()
    else:
        program_selection()

program_selection()