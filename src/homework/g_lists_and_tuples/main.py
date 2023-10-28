import lists

def p_distance_menu():
    
    print("1 - Get p distance matrix")
    print("2 - Exit")

def p_distance_options():

    p_distance_menu()
    opt = input("Please make a selection: ")

    if opt == "1":
        run_p_dist_matrix()
    elif opt == "2":
        print("Exiting program. Goodbye!")
    else:
        print("Please type 1 or 2.")
        p_distance_options()

def run_p_dist_matrix():
    list_row = ""
    list = []
    acceptable_chars = ['A','T','C','G']
    print("Please enter your DNA strings.\n * Please enter as a continous string (e.g., TTTCCATTTA).\n "
                        "* DNA strings will automatically concatenate into a list.\n "
                        "* Strings must be of the same length.\n "
                        "* Must contain only DNA nucleotide characters.\n "
                        "* To complete entry, type DONE.\n")
    
    while list_row != "DONE":
  
        list_row = input("Enter your DNA string here: ")
        validation = [i in acceptable_chars for i in list_row]
        
        if list_row.upper() == "DONE":
            break
        elif all(validation) != True:
            print("Must contain only DNA nucleotides (A, T, C, G). Try your input again.")
            continue
        else:
            list_row_upper = list_row.upper()
            list.append(list_row_upper)
    

    matrix = lists.get_p_distance_matrix(list)
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

    cont = input("Calculate another distance matrix? 2 to exit to the main menu, any other key to continue: ")
    
    if cont != "2":
        run_p_dist_matrix()
    else:
        p_distance_options()
        
p_distance_options()