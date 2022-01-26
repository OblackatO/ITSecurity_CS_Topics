"""
BSF overview.
- Visits all nodes and saves children of visited nodes.
- Does the same thing for each child node.
- If some child node is already in the Queue of found nodes, skip it
"""

# Input and figure extracted from https://favtutor.com/blogs/breadth-first-search-python

from typing import Dict, List

graph: Dict[str, List[str]] = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}


def get_queue(graph):
    queue = []
    for vertice in graph:
        if vertice not in queue:
            queue.append(vertice)
        for child in graph[vertice]:
            if child not in queue:
                queue.append(child)
    return queue

if __name__ == "__main__":
    print(f"BFS queue {get_queue(graph)}")