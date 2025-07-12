# 手写最小堆
import csv

class MinHeap:
    def __init__(self):
        self.data = []
    
    def push(self, item):
        self.data.append(item)
        self._siftup(len(self.data) - 1)
    
    def pop(self):
        if len(self.data) == 0:
            raise IndexError('pop from empty heap')
        self._swap(0, len(self.data) - 1)
        item = self.data.pop()
        self._siftdown(0)
        return item
    
    def _siftup(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.data[parent][0] > self.data[idx][0]:
                self._swap(parent, idx)
                idx = parent
            else:
                break

    def _siftdown(self, idx):
        n = len(self.data)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx
            if left < n and self.data[left][0] < self.data[smallest][0]:
                smallest = left
            if right < n and self.data[right][0] < self.data[smallest][0]:
                smallest = right
            if smallest != idx:
                self._swap(idx, smallest)
                idx = smallest
            else:
                break

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def __len__(self):
        return len(self.data)

# Dijkstra算法（依赖上面的MinHeap）
def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0

    heap = MinHeap()
    heap.push((0, start))

    while len(heap):
        current_dist, u = heap.pop()
        if current_dist > dist[u]:
            continue
        for v in graph[u]:
            alt = current_dist + graph[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heap.push((alt, v))
    return dist, prev

def reconstruct_path(prev, start, end):
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()
    return path if path[0] == start else []

def read_graph_from_csv(file_path):
    graph = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue
            src = row[0]
            dests = row[1:]
            graph[src] = {}
            for dest in dests:
                if ':' in dest:
                    d, w = dest.split(':')
                    graph[src][d] = int(w)
    return graph

def load_graph_from_csv(filename):
    """从CSV文件加载图数据"""
    graph = {}
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            source = row['source']
            destination = row['destination']
            weight = int(row['weight'])
            
            if source not in graph:
                graph[source] = {}
            graph[source][destination] = weight
            
            # 确保目标节点也在图中（即使没有出边）
            if destination not in graph:
                graph[destination] = {}
    
    return graph

def main():
    # 从CSV文件加载图数据
    graph = load_graph_from_csv('graph_edges.csv')
    start = 'A'
    end = 'E'

    # 从CSV文件读取图数据
    # graph = read_graph_from_csv('path_to_your_file.csv')
    
    dist, prev = dijkstra(graph, start)
    path = reconstruct_path(prev, start, end)

    print(f"Shortest distance from {start} to {end}: {dist[end]}")
    print(f"Path: {' -> '.join(path)}")

if __name__ == "__main__":
    main()
