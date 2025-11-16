import random
# รับค่า
graph_data = []
while True:
    start = input("Start: ")
    finish = input("Finish: ")
    dist = int(input("Distance: "))
    if dist == 0:
        break
    graph_data.append({'start': start, 'finish': finish, 'distance': dist})

nodes = set()
for i in graph_data:
    nodes.add(i['start'])
    nodes.add(i['finish'])

nodes = list(nodes)
# เปลี่ยนตัวอักษรเป็นตัวเลข
node_to_id = {nodes[i]: i for i in range(len(nodes))}


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

prim()
kruskal(graph_data)
