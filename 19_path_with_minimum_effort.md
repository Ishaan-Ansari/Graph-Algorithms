# 19. Path With Minimum Effort 

## Problem Statement
<p>You are a hiker preparing for an upcoming hike. You are given <code>heights</code>, a 2D array of size <code>rows x columns</code>, where <code>heights[row][col]</code> represents the height of cell <code>(row, col)</code>. You are situated in the top-left cell, <code>(0, 0)</code>, and you hope to travel to the bottom-right cell, <code>(rows-1, columns-1)</code> (i.e., <strong>0-indexed</strong>). You can move <strong>up</strong>, <strong>down</strong>, <strong>left</strong>, or <strong>right</strong>, and you wish to find a route that requires the minimum <strong>effort</strong>.</p>

<p>A route's <strong>effort</strong> is the <strong>maximum absolute difference</strong> in heights between two consecutive cells of the route.</p>

<p>Return <i>the minimum <strong>effort</strong> required to travel from the top-left cell to the bottom-right cell.</i></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> heights = [[1,2,2],[3,8,2],[5,3,5]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
</pre>
| | | |
|---|---|---|
| 1 | 2 | 2 |
| 3 | 8 | 2 |
| 5 | 3 | 5 |

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> heights = [[1,2,3],[3,8,4],[5,3,5]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
</pre>
| | | |
|---|---|---|
| 1 | 2 | 3 |
| 3 | 8 | 4 |
| 5 | 3 | 5 |


<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> This route does not require any effort.
</pre>
| | | |	| |
|---|---|---|---|---|
| 1 | 2 | 1 | 1 | 1 |
| 1 | 2 | 1 | 2 | 1 |
| 1 | 2 | 1 | 2 | 1 |
| 1 | 2 | 1 | 2 | 1 |
| 1 | 1 | 1 | 2 | 1 |

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>rows == heigh.length</code></li>
	<li><code>columns == heights[i].length</code></li>
	<li><code>1 &lt;= rows, columns &lt;= 100</code></li>
    <li><code>1 &lt;= heights[i][j] &lt;= 10<sup>6</sup></code></li>
</ul>

## Intuition
- The initial brute force that I can think of right now is to do a BFS, But how will you ensure that the path it will take will be of maximum absolute difference.
- Or else what can I do is trace all the possible shortes path from `src` to `dest` and simultaneously keep track of MADiff 
- The path that will have MADiff will eventually be our final answer, But here's the catch if you apply this approach and try to explor every possible valid path the number of operation will be massive (roughly  $O(4^{N})$ where $N$ is the number of cells)
- The optimal approach wpuld be to adapt Dijistra's Algo. instead of summing up distances, we will track the max effort to reach each cell


## Code 
```python
import heapq 

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
		rows, col = len(heights), len(height[0])
		directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

		# min-heap stores tuples of (current_max_effort, row, col)
		min_heap = [(0, 0, 0)]

		# Track min effort to reach each cell
		effort_to = [[float('inf')*col for _ in range(rows)]]
		effort_to[0][0] = 0

		while min_heap:
			effort, r, c = heapq.heappop(min_heap)

			if r = rows-1 and c == col-1:
				return effort

			# we've already found a better path to this cell already, we can skip
			if effort > effort_to[r][c]:
				continue

			for dr, dc in directions:
				nr, nc = r+dr, c+dc

				if 0 <= nr < rows and 0<= nc < cols:
					current_step_effort = abs(heights[r][c] - heights[nr][nc])
					new_max_effort = max(effort, current_step_effort)

				if new_max_effort < effort_to[nr][nc]:
					effort_to[nr][nc] = new_max_effort
					heapq.heappush(min_heap, (new_max_effort, nr, nc))


		return 0
```

## Complexity Analysis
* **Time Complexity:** 
- $O(M \cdot N \log(M \cdot N))$

* **Space Complexity:**
- $O(M \cdot N)$