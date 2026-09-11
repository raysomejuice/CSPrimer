import string

def verify(digits:str) -> bool:
    '''Verify via the Luhn algorithm that a string of decimal digits are valid.
    
    :param digits: str - The string of decimal digits that need to be verified.
    :return: bool - Return true if the string of decimal digits is valid.
    '''
    luhn_total = 0
    reversed_digits = [int(digit) for digit in digits[::-1]]
    for index in range(reversed_digits):
        if index % 2 != 0:
            reversed_digits[index] *= 2
        if reversed_digits > 9:
            reversed_digits[index] -= 9

    return sum(reversed_digits) % 10 == 0 



    if __name__ == '__main__':
        assert verify("17893729974")
        assert not verify("17893729975")
        print("OK")
        
