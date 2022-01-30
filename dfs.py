# Input and figure extracted from https://favtutor.com/blogs/breadth-first-search-python

from typing import Dict, List


# Using a Python dictionary to act as an adjacency list
graph: Dict[str, List[str]] = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

"""
DFS My version.
"""
def bfs_my_version(graph: Dict[str, List[str]], visited: List[str], node: str):
    if node not in visited:
        visited.append(node)
        for child in graph[node]:
            bfs_my_version(graph, visited, child)
        print(f"Temp DFS list: {visited}")
        return visited


print("FINAL DFS list:", bfs_my_version(graph, [], list(graph.items())[0][0]))