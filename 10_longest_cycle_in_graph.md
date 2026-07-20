# 08. Cycle Detection in a directed Graph 

## Problem Statement
> You are given a **directed** graph of `n` nodes numbered from `0` to `n - 1`, where each node has at most one outgoing edge. \
> The graph is represented with a given **0-indexed** array `edges` of size `n`, indicating that there is a directed edge from node `i` to node `edges[i]`. If there is no outgoing edge from node `i`, then `edges[i] == -1`. \
> Return the length of the longest cycle in the graph. If no cycle exists, return `-1`. \
> A cycle is a path that starts and ends at the same node.



## Intuition

## Code 

```python
class Solution:
    def __init__(self):
        self.max_cycle = -1

    def _dfs(self, node, edges, visited, in_path, dist):
        if not visited[node]:
            visited[node] = 1
            in_path[node] = dist
            dist += 1

            neighbor = edges[node]
            if neighbor != -1:
                if not visited[neighbor]:
                    self._dfs(neighbor, edges, visited, in_path, dist)

                elif in_path[neighbor]:
                    current_dist = dist-in_path[neighbor]
                    self.max_cycle = max(self.max_cycle, current_dist)
            
            in_path[node] = 0
            dist = 0

    def longestCycle(self, edges: List[int]) -> int:
        N = len(edges)
        visited = [0]*N
        in_path = [0]*N

        for i in range(N):
            if not visited[i]:
                self._dfs(i, edges, visited, in_path, 1)

        return self.max_cycle
```

## Complexity Analysis
* **Time Complexity:** **O(V + E)** — in the worst case, you visit every vertex and every edge.
* **Space Complexity:** **O(V)** — required for the `visited` array and the recursion stack
