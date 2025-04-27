import heapq
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge("Київ", "Львів", weight=540)
G.add_edge("Київ", "Харків", weight=480)
G.add_edge("Київ", "Одеса", weight=475)
G.add_edge("Київ", "Дніпро", weight=480)
G.add_edge("Львів", "Івано-Франківськ", weight=150)
G.add_edge("Львів", "Ужгород", weight=270)
G.add_edge("Харків", "Дніпро", weight=210)
G.add_edge("Харків", "Запоріжжя", weight=280)
G.add_edge("Дніпро", "Запоріжжя", weight=85)
G.add_edge("Дніпро", "Миколаїв", weight=310)
G.add_edge("Миколаїв", "Одеса", weight=130)
G.add_edge("Чернігів", "Київ", weight=150)
G.add_edge("Полтава", "Харків", weight=140)
G.add_edge("Вінниця", "Київ", weight=260)
G.add_edge("Житомир", "Київ", weight=140)
G.add_edge("Чернівці", "Івано-Франківськ", weight=130)
G.add_edge("Тернопіль", "Львів", weight=140)

adj_list = {node: dict(G[node]) for node in G.nodes}

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            weight = weight['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

print(dijkstra(adj_list, 'Київ'))

pos = nx.spring_layout(G)
options = {
    "node_color": "lightgreen",
    "edge_color": "lightblue",
    "node_size": 500,
    "font_size": 10,
    "font_weight": "normal",
    "width": 2,
    "with_labels": True
}
nx.draw(G, pos, **options)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Транспортна мережа обласних центрів України")
plt.show()