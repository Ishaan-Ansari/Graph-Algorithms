# 07. Cycle Detection in a Undirected Graph 

## Problem Statement
> Given an undirected graph with `V` vertices and `E` edges, represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not.
> Note: The graph can have multiple component. 

## Intuition
Provide a high-level overview of the thought process behind your solution. 
*Why does this approach work?* For instance, you might explain that in a Depth First Search (DFS), if you encounter a node that has already been visited and is not the immediate parent of the current node, a cycle must exist.

## Approach
Break down your algorithm into clear, logical steps:
1. Initialize a `visited` array to keep track of processed nodes.
2. Loop through all vertices from `0` to `V-1` to ensure disconnected components are handled.
3. For each unvisited vertex, initiate a Breadth-First Search (BFS) or Depth-First Search (DFS).
4. During traversal, keep track of the `parent` node. If an adjacent node is already visited and is *not* the parent, return `True`.
5. If the traversal completes without finding such a node, return `False`.

## Code Implementation

```python
from collections import defaultdict

class Solution:
    def _dfs(self, source, lst, visited, parent):
        if not visited[source]:
            visited[source] = 1
            for neighbor in lst[source]:
                if neighbor == parent:
                    continue
                if not visited[neighbor]:
                    if self._dfs(neighbor, lst, visited, source):
                        return True
                else:
                    return True
            else:
                return False
            
	def isCycle(self, V, edges):
		#Code here
		lst = defaultdict(list)
		visited = [0]*V
		
		for u, v in edges:
		    lst[u].append(v)
		    lst[v].append(u)
		    
		for i in range(V):
		    if not visited[i]:
    		    if self._dfs(i, lst, visited, -1):
    		        return True
		 
		return False
```

## Complexity Analysis
* **Time Complexity:** **O(V + E)** — Explain why (e.g., in the worst case, you visit every vertex and every edge).
* **Space Complexity:** **O(V)** — Explain the space overhead (e.g., required for the `visited` array and the recursion stack or queue).
