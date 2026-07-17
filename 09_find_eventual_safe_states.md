# 09. Find Eventual Safe States

## Problem Statement

> There is a directed graph of `n` nodes with each node labeled from `0` to `n - 1`. The graph is represented by a 0-indexed 2D integer array `graph` where `graph[i]` is an integer array of nodes adjacent to node `i`, meaning there is an edge from node `i` to each node in `graph[i]`.
>
> A node is a **terminal node** if there are no outgoing edges.
>
> A node is a **safe node** if every possible path starting from that node leads to a terminal node (or another safe node).
>
> Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

### Example 1

```python
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]

Explanation:
The given graph is shown above.

Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.

Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
```

### Example 2

```python
Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]

Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
```

---

## Intuition

- ~~My initial thoughts about this problem are~~
    - ~~I'll start with DFS, and that DFS function will have parameters like~~

      ```python
      self._dfs(node, adj_lst, visited, parent)
      ```

- ~~Inside my for loop in DFS function I'll check if any directed node is pointing towards empty array, then that will be our terminal node and the parent of it would be the safe state~~

- ~~Once I identified the parent and terminal node I'll append them in the resultant array, I'll do this for all the vertices~~

- ~~And finally I'll return the sorted resultant array.~~

- There was a logical flaw in my initial thoughts:
    - Imagine a node **A** that acts as a fork (**Ψ**):
        - Path 1 goes to a terminal node.
        - Path 2 goes into an endless cycle.

    - If we only check whether node **A** connects to a terminal node, we might mistakenly classify it as **safe**, whereas **A** is actually **unsafe**.

- Instead of looking for terminal nodes, we can look for **cycles**.

- So, this problem is basically a disguised version of **Cycle Detection in a Directed Graph**.

---

## Code

```python
class Solution:
    def __init__(self):
        self.ans = []

    def _dfs(self, node, graph, visited, path, check):
        if not visited[node]:
            visited[node] = 1
            path[node] = 1

            # Assume it is unsafe (0) until it proves all its paths are safe
            check[node] = 0

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if self._dfs(neighbor, graph, visited, path, check):
                        return True

                # neighbor IS visited, check if it is in our active path (Cycle!)
                elif path[neighbor] == 1:
                    return True

                # neighbor IS visited, check if it was previously proven unsafe
                elif check[neighbor] == 0:
                    return True

            check[node] = 1
            path[node] = 0  # Permanently mark as a proven safe state

        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)

        visited = [0] * N
        path = [0] * N

        # For proven safe nodes
        check = [0] * N

        for i in range(N):
            if not visited[i]:
                self._dfs(i, graph, visited, path, check)

        for i in range(N):
            if check[i] == 1:
                self.ans.append(i)

        return self.ans
```

---

## Complexity Analysis

- **Time Complexity:** **O(V + E)** — in the worst case, every vertex and every edge is visited exactly once.
- **Space Complexity:** **O(V)** — required for the `visited`, `path`, and `check` arrays, along with the recursion stack.