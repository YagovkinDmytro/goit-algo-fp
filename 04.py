import uuid

import networkx as nx
import matplotlib.pyplot as plt


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


# # Створення дерева
# root = Node(0)
# root.left = Node(4)
# root.left.left = Node(5)
# root.left.right = Node(10)
# root.right = Node(1)
# root.right.left = Node(3)

# #Відображення дерева
# draw_tree(root)

# Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.

class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break
    
    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)
    
    def heapify_down(self, index):
        size = len(self.heap)
        while 2 * index + 1 < size:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = left
            if right < size and self.heap[right] < self.heap[left]:
                smallest = right
            if self.heap[index] <= self.heap[smallest]:
                break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest
    
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return root
    
    def build_heap(self, elements):
        self.heap = elements
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify_down(i)

# Функція для візуалізації бінарної купи:
def draw_heap(heap_root):
    tree = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    tree = add_edges(tree, heap_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення і візуалізація бінарної купи:

# Створення мінімальної купи
heap = MinHeap()
heap.insert(10)
heap.insert(15)
heap.insert(30)
heap.insert(5)
heap.insert(20)
heap.insert(50)


# Створення дерева з купи
root = Node(heap.heap[0])  # Перший елемент купи — корінь дерева
nodes = [root]

for i in range(1, len(heap.heap)):
    node = Node(heap.heap[i])
    nodes.append(node)

# Побудова дерева для візуалізації
for i in range(len(nodes)):
    if 2 * i + 1 < len(nodes):  # Лівий нащадок
        nodes[i].left = nodes[2 * i + 1]
    if 2 * i + 2 < len(nodes):  # Правий нащадок
        nodes[i].right = nodes[2 * i + 2]

# Візуалізація дерева
draw_tree(root)