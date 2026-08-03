# 13. Largest Color Value in a Directed Graph 

## Problem Statement
There is a <b>directed graph</b> of `n` colored nodes and `m` edges. The nodes are numbered from `0` to `n - 1`.

You are given a string <code>colors</code> where `colors[i]` is a lowercase English letter representing the <b>color</b> of the `ith` node in this graph (<b>0-indexed</b>). You are also given a 2D array `edges` where `edges[j] = [aj, bj]` indicates that there is a <b>directed edge</b> from node `aj` to node `bj`.

A valid <b>path</b> in the graph is a sequence of nodes `x1 -> x2 -> x3 -> ... -> xk` such that there is a directed edge from `xi` to `xi+1` for every `1 <= i < k`. The <b>color value</b> of the path is the number of nodes that are colored the <b>most frequently</b> occurring color along that path.

Return the <em>largest color value</em> of any valid path in the given graph, or `-1` if the <em>graph contains a cycle</em>.

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
<strong>Output</strong>: 3
<strong>Explanation</strong>: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input</strong>: colors = "a", edges = [[0,0]]
<strong>Output</strong>: -1
<strong>Explanation</strong>: There is a cycle from 0 to 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>n == colors.length</code></li>
    <li><code>m == edges.length</code></li>
    <li><code>1 <= n <= 10^5</code></li>
    <li><code>0 <= m <= 10^5</code></li>
    <li><code>colors</code> consists of lowercase English letters.</li>
    <li><code>0 <= aj, bj < n</code></li>
</ul>

## Intuition
- So my initial intuition about this problem is to perform a DFS from each node and calculate the most frequently occuring color
    - But here is catch, suppose there's that meets at a junction and then have a common path
    - As per my initial intuition I've to calculate the frequency for that portion multiple times?

> [!NOTE]
> Since this problem involves DP along with topo sort I'll be skipping it for now [03/08/2026].

## Code 

```python
from collections import defaultdict

class Solution:
    def __init__(self):
        self.ans = 0

    def _dfs(self, adj_lst, visited, node):
        if not visited[node]:
            visited[node] = 1

            for neighbor in adj_lst[node]:
                if not visited[node]:
                    self._dfs(adj_lst, visited, neighbor)

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj_lst = defaultdict(list)

        for u, v in edges:
            adj_lst[u].append(v)

        self.max_freq = 0
        self.has_cycle = False

        path_visited = [False] * n

        current_counts = [0]*26

        def _dfs(node):
            if self.has_cycle:
                return

            if path_visited[node]:
                self.has_cycle = True
                return

            path_visited[node] = True
            color_idx = ord(colors[node])-ord('a')
            current_counts[color_idx] += 1

            self.max_freq = max(self.max_freq, current_counts[color_idx])

            for neighbor in adj_lst[node]:
                _dfs(neighbor)

            path_visited[node] = False
            current_counts[color_idx] -= 1

        for i in range(n):
            if self.has_cycle:
                break
            _dfs(i)

        return -1 if self.has_cycle else self.max_freq        
```

## Complexity Analysis
In graph theory problems, it is standard to express time and space complexity in terms of $V$ (Vertices/Nodes, which is `numCourses`) and $E$ (Edges, which is the number of pairs in `prerequisites`).

* **Time Complexity:** 

* **Space Complexity:**
