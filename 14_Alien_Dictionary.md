# 13. Alien Dictionary 

## Problem Statement

## Intuition

## Code 

```python
from collections import defaultdict

class Solution:
    def findOrder(self, words: list[str]) -> str:
        # We compare adjacent words, scanning left to right, 
        # looking for the very first difference
        
        edges = []
        
        for i in range(1, len(words)):
            preceeding_word = words[i-1]
            succeeding_word = words[i]
        
            min_length = min(len(preceeding_word), len(succeeding_word))
            
            # find the first different char.
            for j in range(min_length):
                if preceeding_word[j] != succeeding_word[j]:
                    edges.append([preceeding_word[j], succeeding_word[j]])
                    break
                
        
        # [[b, a], [d, a], [a, c], [b, d]]
        
        # Now we've to perform topo sort
        adj_lst = defaultdict(list)
        indegree = {char: 0 for word in words for char in word}
        
        for u, v in edges:
            adj_lst[u].append(v)
            indegree[v] += 1
        
        
        ordered_char = deque([char for char, count in indegree.items() if count == 0])

        final_word = []
        
        while ordered_char:
            node = ordered_char.popleft()
            final_word.append(node)
            
            for neighbor in adj_lst[node]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    ordered_char.append(neighbor)
                    
        if len(final_word) != len(indegree):
            return ""
            
        return "".join(final_word)                
```

## Complexity Analysis
In graph theory problems, it is standard to express time and space complexity in terms of $V$ (Vertices/Nodes, which is `numCourses`) and $E$ (Edges, which is the number of pairs in `prerequisites`).

* **Time Complexity:** 

* **Space Complexity:**
