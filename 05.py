import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
    if node.left:
      graph.add_edge(node.id, node.left.id)
      l = x - 1 / 2 ** layer
      pos[node.left.id] = (l, y - 1)
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph


def draw_tree(tree_root):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()

def dfs_tree(root):
    visited_nodes = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node is not None:
            visited_nodes.append(node)
            # Спочатку додаємо **правий** вузол, потім **лівий**, щоб лівий оброблявся першим
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return visited_nodes 
    

def bfs_tree(root):
    visited_nodes = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is not None:
            visited_nodes.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return visited_nodes


def assign_colors(visited_nodes):
    n = len(visited_nodes)
    for i, node in enumerate(visited_nodes):
        intensity = int(50 + (i / max(1, n-1)) * (255 - 50))
        hex_color = f'#{intensity:02x}{intensity:02x}F0'
        node.color = hex_color


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

#Відображення дерева
dfs_visited_nodes = dfs_tree(root)
bfs_visited_nodes = bfs_tree(root)

assign_colors(dfs_visited_nodes)
print("DFS traversal visualization:")
draw_tree(root)

assign_colors(bfs_visited_nodes)
print("BFS traversal visualization:")
draw_tree(root)