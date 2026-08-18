# 19. Path With Minimum Effort 

## Problem Statement
<p>You are a hiker preparing for an upcoming hike. You are given <code>heights</code>, a 2D array of size <code>rows x columns</code>, where <code>heights[row][col]</code> represents the height of cell <code>(row, col)</code>. You are situated in the top-left cell, <code>(0, 0)</code>, and you hope to travel to the bottom-right cell, <code>(rows-1, columns-1)</code> (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.</p>

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

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> heights = [[1,2,3],[3,8,4],[5,3,5]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> This route does not require any effort.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>rows == heigh.length</code></li>
	<li><code>columns == heights[i].length</code></li>
	<li><code>prerequisites[i].length == 2</code></li>
	<li><code>1 &lt;= rows, columns &lt;= 100</code></li>
    <li><code>1 &lt;= heights[i][j] &lt;= 10<sup>6</sup></code></li>
</ul>

## Intuition
- 


## Code 

```python
```

## Complexity Analysis
* **Time Complexity:** 

* **Space Complexity:**
