import decisions

result = decisions.is_overtime(30)

if(result == False):
    print('30 is not overtime')

if(result):
    print('Is overtime')
else:
    print('Not overtime.')