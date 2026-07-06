"""
Given a square chessboard of size (n x n), the initial position and target postion of Knight are given. 
Find out the minimum steps a Knight will take to reach the target position.
"""
from collections import deque

class Solution:
	def minStepToReachTarget(self, KnightPos, TargetPos, n):
		if KnightPos[0] == TargetPos[0] and KnightPos[1] == TargetPos[1]:
			return 0
		
		dx = [2, 2, -2, -2, 1, 1, -1, -1]
		dy = [-1, 1, -2, 2, -2, 2, -1, 1]

		q = deque()
		q.append((KnightPos[0], KnightPos[1], 0))

		visited = [[False for _ in range(n+1)] for _ in range(n+1)]

		visited[KnightPos[0]][KnightPos[1]] = True

		while q:
			curr_x, curr_y, steps = q.popleft()

			for i in range(8):
				new_x = curr_x + dx[i]
				new_y = curr_y + dy[i]
				
				# Check if the next move is the target 
				if new_x == TargetPos[0] and new_y == TargetPos[1]:
					return steps + 1
				
				# Check if the next move is inside the board and hasn't been visited yet
				if 1 <= new_x <= n and 1 <= new_y <= n and not visited[new_x][new_y]:
					visited[new_x][new_y] = True
					q.append((new_x, new_y, steps + 1))

		return -1
	
if __name__ == "__main__":
		solution = Solution()
		KnightPos = [4, 5]
		TargetPos = [1, 1]
		n = 6
		print(solution.minStepToReachTarget(KnightPos, TargetPos, n))  