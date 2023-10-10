def display_list():
    list1 = [5, 10, 20]
    print(list1)

def display_list_w_while():
    list1 = [5, 10, 20]
    i = 0
    while i < len(list1):
        print(list1[i])
        i += 1

def display_reverse_list_w_while():
    list1 = [5, 10, 20]
    i = len(list1) - 1
    while i >= 0:
        print(list1[i])
        i -= 1

def display_list_w_for_range():
    list1 = [5, 10, 20, 3, 7, 1, 50]
    for i in range(0, len(list1)):
        print(list1[i])

def display_list_w_for_range_w_step():
    list1 = [5, 10, 20, 3, 7, 1, 50]
    for i in range(0, len(list1), 2):
        print(list1[i])

def display_list_w_for_range_reverse():
    list1 = [5, 10, 20]
    for i in range(len(list1), 0, -1):
        
        print(list1[i-1])