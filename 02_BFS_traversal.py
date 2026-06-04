from collections import defaultdict, deque

class BFS:
    def __init__(self, adj_list):
        self.adj_list = adj_list

    def traverse(self, start):
        visited = [0]*len(self.adj_list)
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if not visited[node]:
                print(node, end=' ')
                visited[node] = 1
                for neighbor in self.adj_list[node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)


edges = [[1,0], [0,2], [0,5], [3,2], [3,4]]

# Create an adjacency list
adj_list = defaultdict(list)
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

obj = BFS(adj_list)
print("BFS Traversal starting from node 0:")
obj.traverse(0)
