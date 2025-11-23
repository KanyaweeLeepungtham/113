import random
from collections import deque

# รับค่า
graph_data = []
while True:
    start = input("Start: ")
    finish = input("Finish: ")
    distance = int(input("Distance: "))
    if distance == 0:
        break
    graph_data.append({"start": start, "finish": finish, "distance": distance})

nodes = set()
for i in graph_data:
    nodes.add(i["start"])
    nodes.add(i["finish"])

nodes = list(nodes)
nodes.sort()  # ← เพิ่ม (แก้ปัญหา set ทำให้ลำดับ node สุ่ม)

# เปลี่ยนตัวอักษรเป็นตัวเลข
node_to_id = {nodes[i]: i for i in range(len(nodes))}
id_to_node = {i: nodes[i] for i in range(len(nodes))}

# 1.
# -----------------------------
# สร้าง adjacency list
# -----------------------------
n = len(nodes)
adj = [[] for _ in range(n)]

for edge in graph_data:
    u = node_to_id[edge["start"]]
    v = node_to_id[edge["finish"]]
    adj[u].append(v)
    adj[v].append(u)  # (ทำให้กราฟเป็น undirected)


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


start_node = input("\nค้นหาจากจุดเริ่มต้น: ")

end_node = input("ค้นหาจนถึงจุดปลายทาง: ")

print("\nผลลัพธ์ BFS:", bfs(start_node))
print("ผลลัพธ์ DFS:", dfs(start_node))


# ===========================
# Dijkstra Algorithm
def dijkstra(start_name, finish_name):
    start = node_to_id[start_name]
    finish = node_to_id[finish_name]

    dist = [float("inf")] * n
    parent = [-1] * n
    visited = [False] * n

    dist[start] = 0

    for _ in range(n):
        u = -1
        m = float("inf")
        for i in range(n):
            if not visited[i] and dist[i] < m:
                m = dist[i]
                u = i
        if u == -1:
            break
        visited[u] = True

        for edge in graph_data:
            s = node_to_id[edge["start"]]
            f = node_to_id[edge["finish"]]
            w = edge["distance"]

            if s == u:
                v = f
            elif f == u:
                v = s
            else:
                continue

            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

    path = []
    cur = finish
    while cur != -1:
        path.append(id_to_node[cur])
        cur = parent[cur]

    path.reverse()
    return dist[finish], path


# ======prim algo====
def prim():
    ans = []
    total_weight = 0

    # สุ่มเลือกราก
    root = random.choice(nodes)
    visited = {root}

    all_nodes = set(nodes)
    # จุดเริ่ม != จุดจบ/ ยังไม่เป็นลูป
    while visited != all_nodes:
        candidate_edges = [
            i
            for i in graph_data
            if (i["start"] in visited and i["finish"] not in visited)
            or (i["finish"] in visited and i["start"] not in visited)
        ]

        if not candidate_edges:  # (กัน Prim ค้าง)
            break

        # หาเส้นที่นนใน้อยที่สุด นน.->จุดเริ่ม ->จุดจบ
        min_edge = min(candidate_edges, key=lambda i: i["distance"])

        ans.append(min_edge)
        total_weight += min_edge["distance"]

        visited.add(min_edge["start"])
        visited.add(min_edge["finish"])

    print("Total Weight(prim) =", total_weight)


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


# ======Kru algo======
def kruskal(graph):
    edges = []
    for i in graph:
        s = node_to_id[i["start"]]
        f = node_to_id[i["finish"]]
        d = i["distance"]
        edges.append((s, f, d))

    # [2] = distance (0=start,1 = finish)
    edges.sort(key=lambda i: i[2])
    # UnionFind ใช้ได้เฉพาะตัวเลข only
    uf = UnionFind(len(nodes))
    mst = []
    total_weight = 0

    # s = start, f = finish, d = distance
    for s, f, d in edges:
        if uf.union(s, f):
            mst.append((s, f, d))
            total_weight += d

    print("Total Weight(kru) =", total_weight)


prim()
kruskal(graph_data)

dist, path = dijkstra(start_node, end_node)
print(f"Dijkstra: distance={dist}, path={path}")
