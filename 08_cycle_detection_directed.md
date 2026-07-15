# 08. Cycle Detection in a directed Graph 

## Problem Statement
> Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not. The graph is represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge from vertex u to v.

## Intuition


## Approach

## Code Implementation

```python
from collections import defaultdict

class Solution:
    def _dfs(self, node, adj_lst, visited, in_stack):
        if not visited[node]:
            visited[node] = 1
            
            in_stack[node] = 1
            
            for neighbor in adj_lst[node]:
                if not visited[neighbor]:
                    if self._dfs(neighbor, adj_lst, visited, in_stack):
                        return True
                        
                elif in_stack[neighbor]:
                    return True
                        
            in_stack[node] = False
            
        return False
                
    def isCyclic(self, V, edges):
        # code here
        adj_lst = defaultdict(list)
        visited = [0]*V
        
        # To track nodes in the current DFS path
        in_stack = [0]*V
        
        # since it's directional graph!
        for u, v in edges:
            adj_lst[u].append(v)
            
        # here we don't need to worry about keeping track of "parent" node
        
        # Looping through all vertices to catch disconnected components
        for i in range(V):
            if not visited[i]:
                if self._dfs(i, adj_lst, visited, in_stack):
                    return True
                    
        return False
```

## Complexity Analysis
* **Time Complexity:** **O(V + E)** — in the worst case, you visit every vertex and every edge.
* **Space Complexity:** **O(V)** — required for the `visited` array and the recursion stack
