# 21. Bellman-Ford Algorithm for Single Source Shortest Path

## Concept / Intuition
- It's single-source shortest path algorithm.
- Used to find the minimum distance from a given source vertex to all. the catch here is 
- This algo can handle -ve edge weights and is also capable of detecting negetive weight cycles

> [!NOTE]
> For an undirected graph with a negative-weight edge, Bellman-Ford is not applicable for shortest paths because that edge can be traversed in both directions, creating a negative cycle of length 2.

## Code 

```python
class Solution:
    def bellmanFord(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        
      

```

## Complexity Analysis

* **Time Complexity:** 

* **Space Complexity:**
