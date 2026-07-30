# 12. Course Schedule II 

## Problem Statement
<p>There are a total of <code>numCourses</code> courses you have to take, labeled from <code>0</code> to <code>numCourses - 1</code>. You are given an array <code>prerequisites</code> where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you <strong>must</strong> take course <code>b<sub>i</sub></code> first if you want to take course <code>a<sub>i</sub></code>.</p>

<ul>
	<li>For example, the pair <code>[0, 1]</code>, indicates that to take course <code>0</code> you have to first take course <code>1</code>.</li>
</ul>

<p>Return <em>the ordering of courses you should take to finish all courses</em>. If there are many valid answers, return <strong>any</strong> of them. If it is impossible to finish all courses, return <strong>an empty array</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0]]
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
<strong>Output:</strong> [0,2,1,3]
<strong>Explanation:</strong> There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 1, prerequisites = []
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= numCourses &lt;= 2000</code></li>
	<li><code>0 &lt;= prerequisites.length &lt;= numCourses * (numCourses - 1)</code></li>
	<li><code>prerequisites[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; numCourses</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>All the pairs <code>[a<sub>i</sub>, b<sub>i</sub>]</code> are <strong>distinct</strong>.</li>
</ul>

## Intuition
- Initial thoughts are analyzing the pattern, since I've done topo. sort previously, I observed that to pick any course what if I find the outdegree of each node and for a happy case where there are no cycles there must be node of which the out degree would be zero.
- That will be our first prerequisite course...
- This problem is actually topological sort in disguise, just understand the intution behind `prerequiste` array

## Code 

```python
from collections import defaultdict

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

adj_lst =  defaultdict(list)
indegree = [0] * numCourses

# create an adjcency list
for u,v in prerequisites:
    adj_lst[v].append(u)
    indegree[u] += 1

print(adj_lst)
print(indegree)

nodes_with_zero_incoming_edges = []

for node in range(len(indegree)):
    if indegree[node] == 0:
        nodes_with_zero_incoming_edges.append(node)

course_order = []
while nodes_with_zero_incoming_edges:
    current_course = nodes_with_zero_incoming_edges.pop()
    course_order.append(current_course)

    for unlocked_course in adj_lst[current_course]:
        indegree[unlocked_course] -= 1

        if indegree[unlocked_course] == 0:
            nodes_with_zero_incoming_edges.append(unlocked_course)

if len(course_order) == numCourses:
    print(course_order)
else:
    print("impossible")        
```

## Complexity Analysis
In graph theory problems, it is standard to express time and space complexity in terms of $V$ (Vertices/Nodes, which is `numCourses`) and $E$ (Edges, which is the number of pairs in `prerequisites`).

* **Time Complexity:** 
    - Iterating through the `prerequisites` array to populate `adj_lst` and `indegree` takes $O(E)$ time
    - Loop iterates through `indegree` array to find nodes with a value of `0` - $O(numCourses)$ or  $O(V)$ (more appropriate)
    - The `while nodes_with_zero_incoming_edges` loop will run until we run out of all nodes that have no incoming edges - $O(V)$
        - Inside while loop you iterate over `adj_lst[current_course]`, it will execute for $O(E)$ time
            - NOTE - It might look $O(V^2)$ since it's nested inside loop but actually it's NOT
    - Total time -  $O(E + V + V + E)$  ~  $O(V + E)$ time

* **Space Complexity:**
    - `adj_lst` - Stores relationship between nodes (courses) - $O(E)$ 
    - `indegree` - Number of nodes - $O(V)$
    - `nodes_with_zero_incoming_edges` - in the worst case it will be $O(V)$
    - `course_order` - $O(V)$
    - Total space is - $O(E + V + V + V)$ ~ $O(V + E)$
