def test_config():
    return True

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

def get_list_total_while(list1):
    index = 0
    sum = 0

    while (index < len(list1)):
        sum += list1[index]
        index += 1

    return sum

def get_list_total_for(list1):
    sum = 0

    for i in range(0, len(list1)):
        sum += list1[i]

    return sum

def list_reference_parameter(list):
    list[0] = 0

def get_list_return_value(list):
    list[0] = 0

    return list

def list_inside_list():
    list1 = [[5, 10, 20], [6, 10, 5], [5, 0, 20]]
    print(list1[0][0])
    list_at_index_0 = list1[0]
    print(list_at_index_0[1])
    list_at_index_2 = list1[2]
    print(list_at_index_2[2])
    

