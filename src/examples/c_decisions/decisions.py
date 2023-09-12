def test_config():
    return True

def is_odd(num1):
    result = num1 % 2 == 1
    return result

def is_vowel(letter):
    result = letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'
    return result

def is_consonant(letter):
    result = letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u'
    return result

def is_overtime(hours):
    result = False
    result = hours > 40
    return result
        
