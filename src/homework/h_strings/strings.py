def get_hamming_distance(dna1, dna2):

    i = 0
    hd = 0
    
    if len(dna1) == len(dna2):
        while i < len(dna1):
            if dna1[i] != dna2[i]:
            
                hd += 1
                i += 1
            
            
            else:
                i += 1

        return hd
    
    else:
        print("DNA strings must be equal length.")
        

def get_dna_complement(dna):
    

    dna = dna.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
    dna = dna.upper()
    dna = dna[::-1]

    return dna

def display_menu():
    print("1 - Get Hamming Distance")
    print("2 - Get Reverse DNA Complement")
    print("3 - Exit")

def run_menu():
    display_menu()
    opt = int(input("Please choose an option from the menu: "))

    handle_menu_option(opt)

def handle_menu_option(opt):

    if opt == 1:
        run_get_hd()
    elif opt == 2:
        run_get_rev_comp()
    elif opt == 3:
        exit
    else:
        print("Please choose a valid option.")
        run_menu()

def run_get_hd():

    
    dna1 = input("Please enter the first DNA sequence: ")
    dna2 = input("Please enter the second DNA sequence: ")
    hd = get_hamming_distance(dna1, dna2)

    print("The Hamming Distance is", hd)
    print("----------------------------------")
    repeat_operation_choice_hd()


def run_get_rev_comp():
    
    dna = org = input("Please enter the DNA sequence you wish to find the reverse complement of: ")
    rev_comp = get_dna_complement(dna)

    print("Your original DNA sequence is:", org)
    print("The reverse complement is:", rev_comp)
    print("--------------------------------------------")
    repeat_operation_choice_rc()

def repeat_operation_choice_hd():

        opt = int(input("Would you like to continue? 1 to re-run this function, 2 to return to the main menu, 3 to exit the program."))

        if opt == 1:

            run_get_hd()

        elif opt == 2:
            
            run_menu()

        elif opt == 3:
            
            exit
        else:
            print("Please choose a valid option.")
            repeat_operation_choice_hd()

def repeat_operation_choice_rc():

    opt = int(input("Would you like to continue? 1 to re-run this function, 2 to return to the main menu, 3 to exit the program."))

    if opt == 1:

        run_get_rev_comp()

    elif opt == 2:
            
        run_menu()

    elif opt == 3:
            
        exit

    else:
        print("Please choose a valid option.")
        repeat_operation_choice_hd()
