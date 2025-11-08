import random
#   รับค่า grapgh
graph_data = []
def add_graph():
    distance = 1
    while distance != 0:
        start = input("Start: ")
        finish = input("Finish: ")
        distance = int(input("Distance:"))
        if distance == 0:
            break
        graph_data.append({
            'start': start,
            'finish': finish,
            'distance': distance,
        })
    print("Graph data:", graph_data)
add_graph()
#prim algo
def prim():
    # สุ่มหาราก
    root = random.choice([edge['start'] for edge in graph_data])
    print("Random start node:", root)
    #หาเส้นที่นน.น้อยที่สุดจากจุด
    
