"""
Given the following array [1,6,10,20,22,40,45,60,67], find the index of x(x = 67), using the binary search algorithm
"""

import typing

def binary_search(list_input: typing.List[int], x: int, lower_bound: int = -1, upper_bound: int = -1):
    """
    The list_input must always be sorted.
    """
    if lower_bound == -1:
        lower_bound = 0
    if upper_bound == -1:
        upper_bound = len(list_input) - 1
    middle = int((lower_bound + upper_bound)/2)
    if list_input[middle] == x:
        print(f"{x} is at index {middle}.")
        return middle
    if list_input[middle] > x:
        return binary_search(list_input, x, lower_bound=lower_bound, upper_bound=middle-1) # All elements > middle-1 can be ignored. Hence the new upper bound.
    return binary_search(list_input, x, lower_bound=middle+1, upper_bound=upper_bound) # All elements < middle+1 can be ignored. Hence the new lower bound.


list_input = [1,6,10,20,22,40,45,60,67]
x = 67
binary_search(list_input, x)