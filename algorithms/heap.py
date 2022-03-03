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

def heapify_min_heap(heap_structure:List[int]):
    for index in range(0, len(heap_structure)-1):
        left_node = heap_structure[2*index+1]
        right_node = heap_structure[2*index+2]
        node_to_compare = None
        if left_node > right_node:
            node_to_compare = right_node
        else:
            node_to_compare = left_node
        if heap_structure[index] > node_to_compare:
            temp_node = heap_structure[index]
            heap_structure[index] = node_to_compare
            node_to_compare = temp_node

            


