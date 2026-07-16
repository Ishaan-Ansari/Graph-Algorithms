# 08. Cycle Detection in a directed Graph 

## Problem Statement
> Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not. The graph is represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge from vertex u to v.

## Intuition
- The initial thought might be to approach it like simple DFS and if we enounter the visited node again then it's a cycle
    - But the catch here is - 
        - Suppose there's a node $A \rightarrow B, B  \rightarrow C$ and then again from $A  \rightarrow C$, does it look like a cycle ?
        - If you run a DFS starting at $A$, you might first travel $A \rightarrow B \rightarrow C$. The algorithm marks $C$ as "visited." When the search backtracks to $A$ and checks its other connecting edge ($A \rightarrow C$), it sees that $C$ is already marked as "visited." and it falsely returns as cycle

- To resolve this we need to have array along side ```visited``` array inorder to distinguish between node we visited sometime ago versus a node that is part of our current path
- ```in_stack``` tracks node in our current ongoing DFS path, we mark a node `True` or `1` when we enter the loop and `False` or `0` when we backtrack out of it
- A true cycle only exists if we encounter a node that is currently marked as ```True``` in our ```in_stack```

## Code 

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
                        
            in_stack[node] = 0
            
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
