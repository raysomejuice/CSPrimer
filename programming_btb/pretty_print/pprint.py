"""Write a recursive implementation of pretty print."""


from typing import Any


def pprint_recursive(array: list[Any], indent=1: int)->str:
    """Pretty prints a nested list containing any type recursively.
    
    :param array: list[Any] - the nested list
    :param indent: int - how many spaces before each print
    :return: str - the pretty print output
    
    >>> pprint_recursive([1, 2, 3, ['a', 'b', ['c'], 'foo'], 2])
    [ 1,
      2,
      3,
      [ 'a',
        'b',
        [ 'c'],
        'foo'],
      4]
    """
    if len(array) == 1:
        print(array[0], "]")
    else:
      

    