def test_config():
    return True

def display_numbers(num):
    cnt = 0

    while cnt < num:
        print("cnt " + str(cnt) + " cnt + 1 " + str(cnt +1) + " num " + str(num))
        cnt = cnt + 1    # a statement that makes the boolean expression false
        print("cnt after adding 1 " + str(cnt))

def sum_of_squares(num): # sum_of_squares(3) 1 * 1 + 2 * 2 + 3 * 3 = 14
    sum = 0

    while num > 0:
        sum = sum + num * num
        num = num - 1 # eventually makes the boolean expression false

    return sum

def prompt_user():
    keep_going = 'y'

    while keep_going == 'y' or keep_going == 'Y':
        keep_going = input("Loop again, type y or Y: ")
