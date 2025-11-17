import random
from collections import deque

# -----------------------------
# รับ input
# -----------------------------
graph_data = []
while True:
    start = input("Start: ")
    finish = input("Finish: ")
    dist = int(input("Distance (0 = stop): "))
    if dist == 0:
        break
    graph_data.append({'start': start, 'finish': finish, 'distance': dist})

# -----------------------------
# สร้าง nodes
# -----------------------------
nodes = set()
for i in graph_data:
    nodes.add(i['start'])
    nodes.add(i['finish'])

nodes = list(nodes)

# -----------------------------
# แปลงชื่อ node → เลข
# -----------------------------
node_to_id = {nodes[i]: i for i in range(len(nodes))}
id_to_node = {i: nodes[i] for i in range(len(nodes))}

# -----------------------------
# สร้าง adjacency list
# -----------------------------
n = len(nodes)
adj = [[] for _ in range(n)]

for edge in graph_data:
    u = node_to_id[edge['start']]
    v = node_to_id[edge['finish']]
    adj[u].append(v)
    # ถ้ากราฟต้องการเป็น undirected ให้เพิ่มบรรทัดนี้:
    # adj[v].append(u)

# -----------------------------
# BFS
# -----------------------------
def bfs(start_name):
    start = node_to_id[start_name]
    visited = [False] * n
    q = deque([start])
    visited[start] = True

    order = []
    while q:
        u = q.popleft()
        order.append(id_to_node[u])

        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

    return order

# -----------------------------
# DFS (recursive)
# -----------------------------
def dfs(start_name):
    start = node_to_id[start_name]
    visited = [False] * n
    order = []

    def dfs_rec(u):
        visited[u] = True
        order.append(id_to_node[u])
        for v in adj[u]:
            if not visited[v]:
                dfs_rec(v)

    dfs_rec(start)
    return order

# ===========================
# Prim Algorithm
# ===========================
def prim():
    ans = []
    total_weight = 0

    # สุ่มเลือกราก
    root = random.choice(nodes)
    visited = {root}

    all_nodes = set(nodes)

    while visited != all_nodes:
        candidate_edges = [
            i for i in graph_data
            if (i['start'] in visited and i['finish'] not in visited)
               or (i['finish'] in visited and i['start'] not in visited)
        ]
        min_edge = min(candidate_edges, key=lambda i: i['distance'])

        ans.append(min_edge)
        total_weight += min_edge['distance']

        visited.add(min_edge['start'])
        visited.add(min_edge['finish'])

    print("\n=== Prim Result ===")
    print("Total Weight =", total_weight)


# ===========================
# Union-Find Structure
# ===========================
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[rb] = ra
            return True
        return False


# ===========================
# Kruskal Algorithm
# ===========================
def kruskal(graph):
    edges = []
    for i in graph:
        s = node_to_id[i['start']]
        f = node_to_id[i['finish']]
        d = i['distance']
        edges.append((s, f, d))

    # [2] = distance (0=start,1 = finish)
    edges.sort(key=lambda i: i[2])
    #UnionFind ใช้ได้เฉพาะตัวเลข only
    uf = UnionFind(len(nodes))
    mst = []
    total_weight = 0

    # s = start, f = finish, d = distance
    for s, f, d in edges:
        if uf.union(s, f):
            mst.append((s, f, d))
            total_weight += d

    print("\n=== Kruskal Result ===")

    print("Total Weight =", total_weight)
    
# -----------------------------
# เริ่มต้น prim / kruskal
# -----------------------------

prim()
kruskal(graph_data)

# -----------------------------
# เริ่มต้น BFS / DFS
# -----------------------------
start_node = input("\nค้นหาจากจุดเริ่มต้น: ")

print("\nผลลัพธ์ BFS:", bfs(start_node))
print("ผลลัพธ์ DFS:", dfs(start_node))
