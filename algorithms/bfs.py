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

"""
BFS My version.
"""
def bfs_my_version(graph):
    queue = []
    visited_nodes = []

    queue.append(list(graph.items())[0][0])
    visited_nodes.append(list(graph.items())[0][0])

    while queue:
        q_head = queue.pop(0) # Gets head of queue
        for child in graph[q_head]:
            if child not in visited_nodes:
                queue.append(child) # Child added to the queue if not yet visited, so we can get his children.
                visited_nodes.append(child)
    return visited_nodes


"""
solution version: https://favtutor.com/blogs/breadth-first-search-python
"""
visited = [] # List for visited nodes.
queue = []     #Initialize a queue
def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


if __name__ == "__main__":
    print(f"BFS queue {bfs_my_version(graph)}")
    bfs(visited, graph, '5')