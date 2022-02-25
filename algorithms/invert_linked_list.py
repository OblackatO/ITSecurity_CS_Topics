import random
from typing import List

class Node:

    def __init__(self, value:int, next_node = None):
        self.value = value
        self.next_node = next_node

values_of_nodes = [random.randint(500,2000) for _ in range(10)]
nodes = []

for value in values_of_nodes:
    nodes.append(Node(value))

for x in range(0, len(nodes)-1):
    if x != len(nodes) - 1:
        nodes[x].next_node = nodes[x+1]

def print_linked_list(node: Node):
    """
    Prints the linked list nodes.
    """
    if node.next_node is not None:
        print(f"Node: {node.value} -- Next node: {node.next_node.value}")
        print_linked_list(node.next_node)

node = nodes[0]
print_linked_list(node)
nodes = None # Force clean PY cache.

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


print("Inverted linked list:")
print_linked_list(invert_linked_list(node))

