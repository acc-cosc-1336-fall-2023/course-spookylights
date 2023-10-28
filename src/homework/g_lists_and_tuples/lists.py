def test_config():
    return True

def get_p_distance(list1, list2):
    x = 0
    p_diff = []
    if len(list1) == len(list2):
        while x < len(list1):
            for index in list1[x]:
                if index not in list2[x]:
                    p_diff.append(index)
                    x += 1
                    
                else:
                    x += 1
        p_dist = len(p_diff) / len(list1)
        return p_dist
    else:
        print("Lists must be the same size. Exiting program.")
        exit()

def get_p_distance_matrix(list):
   
    p_distance_matrix = []
       
    for x in list:
      
        p_distance_matrix_row = []
    
        for y in list:
          
            p_distance_matrix_row.append(get_p_distance(x, y))

        p_distance_matrix.append(p_distance_matrix_row)

    return p_distance_matrix