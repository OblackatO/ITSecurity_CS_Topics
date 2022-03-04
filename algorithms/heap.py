"""
General idea:
- Generate x random numbers
- Build a tree with those numbers, which are not neessirely ordered.
- Heapify the heap (max/min heap?). Can be a list.
  root: i
    left child: 2i+1
    right child: 2i+2
- Delete node function
- Insert node function

Questions:
- Can I have nodes which are equal on the same level? Like 3-3?
"""

import random
from typing import List

heap_structure = [random.randint(0, 10) for _ in range(0,10)]

def heapify_min_heap(heap_structure:List[int], index: int = -1):
    if index == -1:
        index = round(len(heap_structure) / 2) - 1
    if index == 0:
        return heap_structure
    for temp_index in reversed(range(index-1, index)):
        print(f"Current index: {temp_index}")
        # Was here. Try to make sure that when nodes are updated, the heap_structure are directly used. 
        current_root = heap_structure[temp_index]
        try:
            left_node = 2 * temp_index + 1
            left_node = heap_structure[left_node]
        except IndexError:
            left_node = None
        try:
            right_node = 2 * temp_index + 2
            right_node = heap_structure[right_node]
        except IndexError:
            right_node = None
        if left_node is None:
            if current_root > right_node:
                temp_node = current_root
                current_root = right_node
                right_node = temp_node
        elif right_node is None:
            if current_root > left_node:
                temp_node = current_root
                current_root = left_node
                left_node = temp_node
        else:
            node_to_compare = None
            if right_node > left_node:
                node_to_compare = left_node
            else:
                node_to_compare = right_node
            if current_root > node_to_compare:
                temp_node = current_root
                current_root = node_to_compare
                node_to_compare = temp_node
    if index == 1:
        return heapify_min_heap(heap_structure, index=0)
    index = round(index/2)
    return heapify_min_heap(heap_structure, index=index)

print(f"Heap structure before heapifying: {heap_structure}")
heapified = heapify_min_heap(heap_structure)
print(f"Heapified tree: {heapified}")




