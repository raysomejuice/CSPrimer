import string

def verify(digits:str) -> bool:
    '''Verify via the Luhn algorithm that a string of decimal digits are valid.
    
    :param digits: str - The string of decimal digits that need to be verified.
    :return: bool - Return true if the string of decimal digits is valid.
    '''
    luhn_total = 0
    for index, digit in enumerate(reversed(digits)):
        digital_root = (1 + index % 2) * int(digit)
        luhn_total += digital_root // 10 + digital_root

    return luhn_total % 10 == 0 
