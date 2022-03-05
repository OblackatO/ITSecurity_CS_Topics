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

heap_structure = [random.randint(0, 500) for _ in range(0,10)]
heap_structure_copy = heap_structure

# My version
####################################################################################################################
def call_heapify(heap_structure):
    for index in range((len(heap_structure)//2)-1, -1, -1):
        heapify_min_heap(heap_structure, index)

def heapify_min_heap(heap_structure:List[int], index:int):
    left_node_index = 2*index + 1
    right_node_index = 2*index + 2
    largest_index = index
    tree_max_index = len(heap_structure) # why not -1 ?
    if tree_max_index > left_node_index and heap_structure[left_node_index] < heap_structure[largest_index]:
        largest_index = left_node_index
    if tree_max_index > right_node_index and heap_structure[right_node_index] < heap_structure[largest_index]:
        largest_index = right_node_index
    if largest_index != index:
        heap_structure[index], heap_structure[largest_index] = heap_structure[largest_index], heap_structure[index]
        heapify_min_heap(heap_structure, largest_index)

def delete_node(heap_structure:List[int], node:int):
    # - If index == index of last node : Just delete node
    # - If index != index of last node : Replace index with index of last node, delete last node and heapify.
    print(f"Heap with node to delete: node: {node} -- heap: {heap_structure}")
    index = heap_structure.index(node)
    if index != len(heap_structure)-1:
        heap_structure[index] = heap_structure[-1]
    heap_structure.pop()
    call_heapify(heap_structure)
    print(f"Heap with node deleted:{heap_structure}")

def insert_node(heap_structure:List[int], node:int):
    print(f"Heap without new node: {node} -- heap: {heap_structure}")
    heap_structure.append(node)
    call_heapify(heap_structure)
    print(f"Heap with new node:{heap_structure}")

print(f"Heap structure before heapifying: {heap_structure}")
for index in range((len(heap_structure)//2)-1, -1, -1):
    heapify_min_heap(heap_structure, index)
print(f"Heapified tree: {heap_structure}")

delete_node(heap_structure, heap_structure[4])
insert_node(heap_structure, 90)
insert_node(heap_structure, 43)
insert_node(heap_structure, 500)
####################################################################################################################


# Version from https://favtutor.com/blogs/heap-in-python
########################################################
def min_heapify(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] < A[k]:
        smallest = l
    else:
        smallest = k
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        min_heapify(A, smallest)

def left(k):
    return 2 * k + 1

def right(k):
    return 2 * k + 2

def build_min_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        min_heapify(A,k)
build_min_heap(heap_structure_copy)
print(heap_structure_copy)
##########################################################
