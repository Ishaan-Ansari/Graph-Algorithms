# 07. Cycle Detection in a Undirected Graph 

## Problem Statement
> Given an undirected graph with `V` vertices and `E` edges, represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not.
> Note: The graph can have multiple component. 

## Intuition

- The hook here is simple, While traversal if you encounter a node that has already been visited and is not immediate parent of the current node, a cycle exist.
- Concept of parent - In case of ```UNDIRECTED GRAPH``` when we are iterating over ```adj_lst``` you'll encounter the node from where you just came from. To avoid false positives, we track this "parent" node and simply skip it during our check. 
- Here false positive means if we don't track parent the program will understand the parent node as a cycle completion and it will return ```True```
- Because undirected edges are bidirectional, traveling from a parent node $A$ to a child node $B$ means $A$ remains in $B$'s neighbor list. Without tracking the parent, the algorithm will look back at $A$, see that it is already visited, mistake this back-and-forth path for a completed cycle, and incorrectly return ```True```.

## Approach
1. Initialize a `visited` array to keep track of processed nodes.
2. Loop through all vertices from `0` to `V-1` to ensure disconnected components are handled.
3. Check if the vertex is NOT visited and then mark it as true.
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
