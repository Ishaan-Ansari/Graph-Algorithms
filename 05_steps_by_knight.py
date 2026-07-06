"""
Given a square chessboard of size (n x n), the initial position and target postion of Knight are given. 
Find out the minimum steps a Knight will take to reach the target position.
"""
from collections import deque

class Solution:
	def minStepToReachTarget(self, KnightPos, TargetPos, n):
		if KnightPos[0] == TargetPos[0] and KnightPos[1] == TargetPos[1]:
			return 0