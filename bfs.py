"""
BSF overview.
- Visits all nodes and saves children of visited nodes.
- Does the same thing for each child node.
- If some child node is already in the Queue of found nodes, skip it
"""

# Input and figure extracted from https://favtutor.com/blogs/breadth-first-search-python

from typing import Dict, List

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

"""
My version.
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
https://favtutor.com/blogs/breadth-first-search-python version
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

# Driver Code
#print("Following is the Breadth-First Search")
#bfs(visited, graph, '5')    # function calling


if __name__ == "__main__":
    print(f"BFS queue {bfs_my_version(graph)}")
    bfs(visited, graph, '5')