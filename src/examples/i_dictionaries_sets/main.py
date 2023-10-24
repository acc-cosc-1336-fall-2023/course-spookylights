#main program
import dictionaries

# languages = {"C#":"OOL","Python":"Easy","JavaScript":"Easy 2"}

# phonebook = {"Chris":"555-1111", "Katie":"555-0222"}

# print(phonebook["Chris"])

# print(phonebook["Katie"])

# for key in phonebook:
#     print(key, phonebook[key])

# print("values only")
# for value in phonebook.values():
#     print(value)

# print("dictionary items")
# for item in phonebook.items():
#     print(item)

#exists = dictionaries.is_key_in_dictionary('Chris', phonebook)

key = input("Enter key: ")
value = input("Enter value: ")
phonebook = {}

phonebook[key] = value

print(phonebook)