"""Adjacency list & matrix implementation"""
from collections import defaultdict

edges = [[1,2], [2,3], [3,4], [4,2], [1,3]]

N = 4

adj_list = defaultdict(list)

for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)  

print(dict(adj_list))

adj_mat = [[0 for _ in range(N)] for _ in range(N)]

for u, v in edges:
    u -= 1
    v -= 1
    adj_mat[u][v] = 1
    adj_mat[v][u] = 1

print(adj_mat)