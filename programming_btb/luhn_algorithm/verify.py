import string

def verify(digits:str) -> bool:
    '''Verify via the Luhn algorithm that a string of decimal digits are valid.
    
    :param digits: str - The string of decimal digits that need to be verified.
    :return: bool - Return true if the string of decimal digits is valid.
    '''
    luhn_total = 0
    reversed_digits = digits[::-1].split()