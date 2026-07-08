from collections import defaultdict

class DFS:
    def __init__(self, adj_list):
        self.adj_list = adj_list

    def traverse(self, start):
        visited = [0]*len(self.adj_list)
        self._dfs_helper(start, visited)

    def _dfs_helper(self, node, visited):
        if not visited[node]:
            print(node, end=' ')
            visited[node] = 1
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    self._dfs_helper(neighbor, visited)

# 1. Create adjacency list
edges = [[1,0], [0,2], [0,5], [3,2], [3,4]]

adj_list = defaultdict(list)

for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

obj = DFS(adj_list)
print("DFS Traversal starting from node 0:")
obj.traverse(0)
