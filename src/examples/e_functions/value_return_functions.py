def test_config():
    return True

def is_number_odd(num):
    return num % 2 == 1

def local_function_variable(val0):
    val = val0
    val1 = 100
    val2 = 10

    return val1

val3 = 5

def global_variable_w_param(val3):
    
    return val3

def global_variable():
    val3 = 10
    return val3

def global_variable_2():
    return val3