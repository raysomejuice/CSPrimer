def verify(digits: str) -> bool:
    '''Verify via the Luhn algorithm that a string of decimal digits are valid.

    The dictionary luhn_map maps the input string digit with its digital root.
    The digital root is calculated for every second digit from the string.
    
    :param digits: str - The string of decimal digits that need to be verified.
    :return: bool - Return true if the string of decimal digits is valid.
    '''
    luhn_map = {'0' : 0, '1' : 2, '2' : 4, '3' : 6, '4' : 8, 
                '5' : 1, '6' : 3, '7' : 5, '8' : 7, '9' : 9}
    
    return sum(luhn_map[digit] if index % 2 == 1 else int(digit) 
           for index, digit in enumerate(reversed(digits))) % 10 == 0
