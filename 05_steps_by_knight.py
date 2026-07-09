"""
Given a square chessboard of size (n x n), the initial position and target postion of Knight are given. 
Find out the minimum steps a Knight will take to reach the target position.
"""
from collections import deque

class Solution:
    def minStepToReachTarget(self, knightPos, targetPos, n):
        # Code here
        if knightPos[0] == targetPos[0] and knightPos[1] == targetPos[1]:
            return 0

        # Initialize a BFS queue storing tuples of (current_x, current_y, steps_taken).
        # We start at the knight's initial position with 0 steps.
        q = deque()
        q.append((knightPos[0], knightPos[1], 0))

        # Create an (n + 1) x (n + 1) grid filled with 0s.
        visited = [[0] * (n + 1) for _ in range(n + 1)]

        visited[knightPos[0]][knightPos[1]] = 1

        dx = [2, 2, 1, 1, -1, -1, -2, -2]
        dy = [1, -1, 2, -2, 2, -2, -1, 1]

        while q:
            curr_x, curr_y, steps = q.popleft()

            for i in range(8):
                new_x = curr_x + dx[i]
                new_y = curr_y + dy[i]

                if new_x == targetPos[0] and new_y == targetPos[1]:
                    return steps + 1

                # Ensure the new position is:
                # - Inside the board boundaries (between 1 and n inclusive)
                # - Not visited yet (to prevent looping backwards)
                if 1 <= new_x <= n and 1 <= new_y <= n and not visited[new_x][new_y]:
                    visited[new_x][new_y] = 1
                    q.append((new_x, new_y, steps + 1))

        return -1
		