def get_factorial(num):
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial * i
    return factorial

def sum_odd_numbers(num):
    sum = 0
    i = num

    while i > 0:
        if i % 2 == 1:
            sum += i
        i -= 1
    return sum

def display_menu():
    print("1- Factorial")
    print("2- Sum Odd Numbers")
    print("3- Exit")

def run_menu():
    display_menu()
    option = input("Enter a menu option(1, 2, or 3): ")

    handle_menu_option(option)

def handle_menu_option(option):
    if(option == "1"):
        selected_option_1()
    elif(option == "2"):
        selected_option_2()
    elif(option == "3"):
        selected_option_3()

def selected_option_1():
    num = int(input("Please input a number: "))

    if num > 0 and num < 10:
        print(get_factorial(num))
        exit = input("Do you want to exit? Type e to exit or hit Enter key to continue.")

        if exit == "e":
            print("Goodbye!")
        else:
            selected_option_1()
    else:
        exit = input("Please input a value greater than zero and less than 10. Otherwise type e to exit or hit Enter key to continue.")
        
        if exit == "e":
                print("Goodbye!")
        else:
                selected_option_1()
        

def selected_option_2():
    num = int(input("Please input a number: "))

    if num > 0 and num < 100:
        print(sum_odd_numbers(num))
        
        exit = input("Do you want to exit? Type e to exit or hit Enter key to continue.")

        if exit == "e":
            print("Goodbye!")
        else:
            selected_option_2()    
    else:
        exit = input("Please input a value greater than zero and less than 99. Otherwise type e to exit or hit Enter key to continue.")

        if exit == "e":
            print("Goodbye!")
        else:
            selected_option_2()
        


def selected_option_3():
    option = input("Type y to continue, or hit Enter key to exit: ")

    if option == "y":
        run_menu()
    else:
        print("Goodbye!")