"""
Given a square chessboard of size (n x n), the initial position and target postion of Knight are given. 
Find out the minimum steps a Knight will take to reach the target position.
"""

from collections import deque

class Solution:
	def minStepToReachTarget(self, knightPos, targetPos, n):
		#Code here
		if knightPos[0]==targetPos[0] and knightPos[1]==targetPos[1]:
		    return 0
		    
        dx = [-2, -2, -1, -1, 1, 1, 2, 2]
        dy = [-1, 1, -2, 2, -2, 2, -1, 1]
		
		q = deque()
		# Queue for BFS: stores (x, y, steps_taken)
		q.append((knightPos[0], knightPos[1], 0))
		
		visited = [[False]*(n+1) for _ in range(n+1)]
		visited[knightPos[0]][knightPos[1]] = True
		
		while q:
		    curr_x, curr_y, steps = q.popleft()
		    
		    for i in range(8):
		        next_x = curr_x + dx[i]
		        next_y = curr_y + dy[i]
		        
		        # check if the next move is the target
		        if next_x == targetPos[0] and next_y == targetPos[1]:
		            return steps + 1
		      
		        # check if the next move is inside the board AND hasn't been visited yet
		        if 1 <= next_x <= n and 1 <= next_y <= n and not visited[next_x][next_y]:
		            visited[next_x][next_y] = True
		            q.append((next_x, next_y, steps+1))
		      
    	return -1
		