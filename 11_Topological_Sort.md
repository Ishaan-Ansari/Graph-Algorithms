# 11. Topological Sort

## Problem Statement
 > Given a Directed Acyclic Graph (DAG) with V vertices labeled from `0` to `V-1`.The graph is represented using an adjacency list where adj[i] lists all nodes connected to node. Find any Topological Sorting of that Graph.

Input: V = 6, adj = [[], [], [3], [1], [0, 1], [0, 2]]  
Output: [5, 4, 2, 3, 1, 0]  

## Intuition
A topological sort takes a directed acyclic graph (`DAG`) and returns its nodes in an order where every node comes before the nodes it points to. It's used for scheduling tasks with dependencies, and it only exists if the graph has <u>no cycles</u>.

```mermaid
graph LR
    1 --> 2
    1 --> 3
    2 --> 4
    2 --> 5
    3 --> 4
    4 --> 5
```

Since node 1 points to nodes 2 and 3, node 1 appears before them in the ordering. And, since nodes 2 and 3 both point to node 4, they appear before it in the ordering. \
So `[1, 2, 3, 4, 5]` would be a topological ordering of the graph.

We'll use the following strategy - 
1. Identify a node with no incoming edges. (indegree => 0)
2. Add that node to the ordering.
3. Remove it from the graph.
4. Repeat.

**NOTE** - Instead of actually removing the nodes from the graph (and destroying our input!), we'll use a hash map to track each node's indegree. When we add a node to the topological ordering, we'll decrement the indegree of that node's neighbors, representing that those nodes have one fewer incoming edges.

## Code 

For this problem the graph looks like

adj = [[], [], [3], [1], [0, 1], [0, 2]]  

```mermaid
graph LR
    5 --> 0
    4 --> 0
    5 --> 2
    2 --> 3
    3 --> 1
    4 --> 1
```

```python
class Solution:
    def topoSort(self, V, adj):
        # First we have calculate the indegree of the nodes
        indegree = {node:0 for node in range(len(adj))}
        for index, neighbors in enumerate(adj):
            for v in neighbors:
                indegree[v] += 1


        # track nodes with no incoming edges
        node_with_no_incoming_edges = []
        for node in adj:
            if indegree[node] == 0:
                node_with_no_incoming_edges.append(node)

        
        # initially no nodes in our ordering
        topological_ordering = []

        # as long as there are nodes with no incoming edges
        # that can be added to the ordering
        while len(node_with_no_incoming_edges) > 0:
            node = node_with_no_incoming_edges.pop()
            topological_ordering.append(node)

            # decrement the indegree of that node's neighbor
            for neighbor in adj[node]
            ...

        # we've run out of nodes with no incoming edges
        if len(topological_ordering) == len(adj):
            return topological_ordering

        else:
            raise Exception("Graph has a cycle! No topological oridering exists.")
```

## Complexity Analysis
* **Time Complexity:** **O(V + E)** — in the worst case, you visit every vertex and every edge.
* **Space Complexity:** **O(V)** — required for the `visited` array and the recursion stack