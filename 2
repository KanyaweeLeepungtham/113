# ===========================
# Dijkstra Algorithm
# ===========================
def dijkstra(start_name, finish_name):
    start = node_to_id[start_name]
    finish = node_to_id[finish_name]

    dist = [float('inf')] * n
    parent = [-1] * n
    visited = [False] * n

    dist[start] = 0

    for _ in range(n):
        u = -1
        m = float('inf')
        for i in range(n):
            if not visited[i] and dist[i] < m:
                m = dist[i]
                u = i
        if u == -1:
            break
        visited[u] = True

        for edge in graph_data:
            s = node_to_id[edge['start']]
            f = node_to_id[edge['finish']]
            w = edge['distance']

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
