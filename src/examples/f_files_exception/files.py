#
def write_to_file(file_name):
    out_file = open(file_name, 'w')

    #write to file
    out_file.write('John Locke\n')
    out_file.write('David Hume\n')
    out_file.write('Edmund Burke\n')

    #close the file
    out_file.close()

def read_from_file(file_name):
    in_file = open(file_name, 'r')

    file_contents = in_file.read()

    #close file
    in_file.close()

    print(file_contents)
    
def read_each_line_from_file(file_name):
    in_file = open(file_name, 'r')

    line1 = in_file.readline()
    line2 = in_file.readline()
    line3 = in_file.readline()

    print(line1.rstrip('\n'))
    print(line2.rstrip('\n'))
    print(line3.rstrip('\n'))

    #close the file
    in_file.close()

def write_name_to_file(file_name):
    out_file = open(file_name, 'w')

    user_choice = ''
    while True:
        name = input('Enter a name: ')
        out_file.write(name+'\n')
        user_choice = input('Do you want to continue?')
        if user_choice.lower() == 'y':
            
            continue
        else:
            out_file.close()
            break

