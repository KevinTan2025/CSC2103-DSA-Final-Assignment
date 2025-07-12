import heapq

def dijkstra(graph, start):
    # 初始化距离和前驱节点
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0

    # 优先队列，元素为 (距离, 节点)
    heap = [(0, start)]

    while heap:
        current_dist, u = heapq.heappop(heap)

        # 如果弹出的距离比记录的大，说明已访问过
        if current_dist > dist[u]:
            continue

        for v, weight in graph[u].items():
            alt = current_dist + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(heap, (alt, v))

    return dist, prev

def reconstruct_path(prev, start, end):
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()
    return path if path[0] == start else []

def main():
    # Sample graph (有向加权图)
    graph = {
        'A': {'B': 10, 'C': 5},
        'B': {'C': 1, 'D': 4},
        'C': {'D': 1},
        'D': {'E': 3},
        'E': {}
    }
    start = 'A'
    end = 'E'

    dist, prev = dijkstra(graph, start)
    path = reconstruct_path(prev, start, end)

    print(f"Shortest distance from {start} to {end}: {dist[end]}")
    print(f"Path: {' -> '.join(path)}")

if __name__ == "__main__":
    main()
