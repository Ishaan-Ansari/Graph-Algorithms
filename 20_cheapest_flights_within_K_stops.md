# 20. Cheapest Flights Within K Stops

## Problem Statement
<p>There are <code>n</code> cities connected by some number of flights. You are given an array flights where <code>flights[i] = [from<sub>i</sub>, to<sub>i</sub>, price<sub>i</sub>]</code> indicates that there is a flight from city <code>from<sub>i</sub></code> to city <code>to<sub>i</sub></code> with cost <code>price<sub>i</sub></code>.</p>

<p>You are also given three integers <code>src</code>, <code>dst</code>, and <code>k</code>, return the cheapest price from <code>src</code> to <code>dst</code> with at most <code>k</code> stops. If there is no such route, return <code>-1</code>.</p>


<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
<strong>Output:</strong> 700
<strong>Explanation:</strong> The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
<strong>Output:</strong> 200
<strong>Explanation:</strong> The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
<strong>Output:</strong> 500
<strong>Explanation:</strong> The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

</pre>


## Intuition

## Code 

```python
import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        # create a adjecency list
        for f, t, p in flights:
            adj[f].append((t, p))

        min_stops = [float('inf')]*n

        hq = []
        # current_cost, current_node, stops_taken
        heapq.heappush(hq, (0, src, 0))

        while hq:
            curr_dist, curr_node, stops = heapq.heappop(hq)

            if curr_node == dst:
                return curr_dist

            # k stops means a maximum of k + 1 flights
            if stops == k+1:
                continue

            # If we've already been to this node with FEWER or EQUAL stops
            if stops >= min_stops[curr_node]:
                continue

            min_stops[curr_node] = stops

            for neighbor, price in adj[curr_node]:
                heapq.heappush(hq, (curr_dist+price, neighbor, stops+1))

        return -1       
```

## Complexity Analysis
* **Time Complexity:** 
* **Space Complexity:**
