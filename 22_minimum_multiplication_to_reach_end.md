# 21. Minimum multiplications to reach end

## Concept / Intuition

## Code 

```python
from collections import deque

class Solution:
    def minimumMultiplications(self, arr, start, end):
        if start == end:
            return 0

        q = deque([(start, 0)])
        visited = [False]*100000
        visited[start] = True

        while q:
            node, steps = q.popleft()

            for multiplier in arr:
                num = (node * multiplier) % 100000
                if not visited[num]:
                    if num == end:
                        return steps+1

                    visited[num] = True
                    q.append((num, steps+1))

        return -1      
```

## Complexity Analysis

* **Time Complexity:** 

* **Space Complexity:**
