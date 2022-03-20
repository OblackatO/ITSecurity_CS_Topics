# Quicksort overview https://www.youtube.com/watch?v=7h1s2SojIRw&t

from typing import List

def quicksort(list_to_sort:List[int]):
    if len(list_to_sort) <= 1:
        return list_to_sort
    pivot = list_to_sort.pop(0)
    bigger_than_pivot = []
    smaller_than_pivot = []
    for element in list_to_sort:
        if element >= pivot:
            bigger_than_pivot.append(element)
        else:
            smaller_than_pivot.append(element)
    return quicksort(smaller_than_pivot) + [pivot] + quicksort(bigger_than_pivot)

print(quicksort([5,9,3,23,12,21,98,4,900,3,23]))