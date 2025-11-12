import random
#   รับค่า grapgh
graph_data = []
distance = 1
while distance > 0:
    start = input("Start: ")
    finish = input("Finish: ")
    distance_input = input("Distance:")
    if distance == 0:
        break
    graph_data.append({
        'start': start,
        'finish': finish,
        'distance': distance,
    })
print("Graph data:", graph_data)


# ======prim algo====

def prim():
    ans = []
    total_weight = 0
    # สุ่มเลือกราก
    root = random.choice([i['start'] for i in graph_data])
    path = {root}
    # เก็บค่า node
    all_nodes = set([i['start'] for i in graph_data] + [i['finish'] for i in graph_data])
    # จุดเริ่ม != จุดจบ/ ยังไม่เป็นลูป
    while path != all_nodes:
        candidate_edges = [
            i for i in graph_data
            if (i['start'] in path and i['finish'] not in path)
               or (i['finish'] in path and i['start'] not in path)
        ]
        # หาเส้นที่นนใน้อยที่สุด นน.->จุดเริ่ม ->จุดจบ
        min_edge = min(candidate_edges, key=lambda e: (e['distance'], e['start'], e['finish']))

        ans.append(min_edge)
        total_weight += min_edge['distance']

        path.add(min_edge['start'])
        path.add(min_edge['finish'])
        print("total_weight(prim)", total_weight)


# ======Kru algo======
def kru():
    # เรียงลำดับนน. -> จุดเริ่ม -> จุดจบ
    root = sorted(graph_data, key=lambda i: (i['distance'], i['start'], i['finish']))
    route = set()
    ans = []
    total = 0

    for i in root:
        # เก็บค่า node
        s = i['start']
        f = i['finish']
        # จุดเริ่ม != จุดจบ/ ยังไม่เป็นลูป
        if s not in route or f not in route:
            ans.append(i)
            route.add(s)
            route.add(f)
    # หาค่า นน.
    total = sum(r['distance'] for r in ans)
    print("Total Weight =", total)

prim()
kru()


