from distutils.command.build_scripts import first_line_re
import random
import sys
from typing import List

sys.setrecursionlimit(20000) # Python recursion is limited to 993 calls.

class Node:

    def __init__(self, value:int, next_node = None):
        self.value = value
        self.next_node = next_node

def build_nodes():
    """Builds a linked list of nodes.
    Returns the 1 node in the linked list.
    """
    values_of_nodes = [random.randint(500,2000) for _ in range(19000)]
    prev_node = None
    first_node = None
    for value in values_of_nodes:
        node = Node(value)
        if prev_node is not None:
            prev_node.next_node = node
        else:
            first_node = node
        prev_node = node
    return first_node

def print_linked_list(node: Node):
    """
    Prints the linked list nodes.
    """
    if node.next_node is not None:
        print(f"Node: {node.value} -- Next node: {node.next_node.value}")
        print_linked_list(node.next_node)


def invert_linked_list(node: Node, prev_node: Node = None):
    if node == None:
        return prev_node
    temp_node = node.next_node
    if prev_node is None:
        node.next_node = None
    else:
        node.next_node = prev_node
    prev_node = node
    return invert_linked_list(node=temp_node, prev_node=prev_node)

def invert_linked_list_exercise_solution(node: Node):
    """Invert a linked list youtube solution.
    https://www.youtube.com/watch?v=XDO6I8jxHtA

    Args:
        node (Node): The starting node.
    """
    prev_node = None
    while node:
        temp = node
        node = node.next_node
        temp.next_node = prev_node
        prev_node = temp
    return prev_node

node = build_nodes()
print(f"Linked list of nodes:")
print_linked_list(node)

print("Inverted linked list:")
print_linked_list(invert_linked_list(node))

node = build_nodes()
print("\n2nd linked list of nodes")
print_linked_list(node)
print("Inverted linked list 2nd version")
print_linked_list(invert_linked_list_exercise_solution(node))

