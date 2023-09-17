import decisions

option = float(input("Please input a value for options: "))

total = float(input("Please input a value for total: "))

result = decisions.get_options_ratio(option, total)

print(decisions.get_faculty_rating(result))
