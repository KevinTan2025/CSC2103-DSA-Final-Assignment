# Custom Min Heap implementation
import csv
import os

# Data source path definition
DATA_PATH = os.path.join(os.path.dirname(__file__), "graph_edges.csv")

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

# Dijkstra algorithm (depends on MinHeap above)
def dijkstra_with_visualization(graph, start):
    """Dijkstra algorithm with visualization"""
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    visited = set()
    dist[start] = 0
    
    heap = MinHeap()
    heap.push((0, start))
    
    step = 0
    print(f"\n{'='*60}")
    print(f"Dijkstra Algorithm - Start: {start}")
    print(f"{'='*60}")
    
    # Display initial state
    print_step_diagram(step, dist, visited, None, None, heap, graph, prev)
    
    while len(heap):
        step += 1
        current_dist, u = heap.pop()
        
        if current_dist > dist[u]:
            continue
            
        if u in visited:
            continue
            
        visited.add(u)
        
        print(f"\nStep {step}: Processing {u}")
        
        # Display current processing node
        print_step_diagram(step, dist, visited, u, None, heap, graph, prev)
        
        # Check all neighboring nodes
        neighbors_updated = []
        
        for v in graph[u]:
            alt = current_dist + graph[u][v]
            
            if alt < dist[v]:
                old_dist = dist[v]
                dist[v] = alt
                prev[v] = u
                heap.push((alt, v))
                neighbors_updated.append((v, old_dist, alt))
        
        # If there are updates, display updated state
        if neighbors_updated:
            print_step_diagram(step, dist, visited, u, neighbors_updated, heap, graph, prev)
        
        input("\nPress Enter to continue...")
    
    print(f"\n{'='*60}")
    print("Algorithm Complete!")
    print(f"{'='*60}")
    print_final_diagram_and_table(dist, prev, start, graph)
    
    return dist, prev

def dijkstra(graph, start):
    """Original Dijkstra algorithm (no visualization)"""
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

def load_graph_from_csv(filename):
    """Load graph data from CSV file"""
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
            
            # Ensure destination node is also in graph (even if no outgoing edges)
            if destination not in graph:
                graph[destination] = {}
    
    return graph

def get_all_nodes(graph):
    """Get all nodes in the graph"""
    nodes = set()
    for source in graph:
        nodes.add(source)
        for destination in graph[source]:
            nodes.add(destination)
    return sorted(list(nodes))

def get_user_input(graph):
    """Get user input for start and end points"""
    nodes = get_all_nodes(graph)
    
    print("Available nodes:", ', '.join(nodes))
    print()
    
    while True:
        start = input("Enter start node: ").strip().upper()
        if start in nodes:
            break
        print(f"Error: Node '{start}' does not exist. Please choose from: {', '.join(nodes)}")
    
    while True:
        end = input("Enter end node: ").strip().upper()
        if end in nodes:
            break
        print(f"Error: Node '{end}' does not exist. Please choose from: {', '.join(nodes)}")
    
    return start, end

def print_step_diagram(step, dist, visited, current_node, updated_neighbors, heap, graph, prev=None):
    """Print graphical display of current step"""
    nodes = get_all_nodes(graph)
    
    # Display Dijkstra table
    print_dijkstra_table(nodes, dist, visited, current_node, prev)
    
    # If neighbors updated, simply display
    if updated_neighbors:
        print(f"\nUpdated:")
        for node, old_dist, new_dist in updated_neighbors:
            old_str = "∞" if old_dist == float('inf') else str(old_dist)
            print(f"  {node}: {old_str} → {new_dist}")

def print_cli_graph(visited, current_node, prev):
    """Draw CLI graph showing current connection status"""
    print(f"\nGraph Connections:")
    print("        (10)        (4)        (3)")
    print("A ---------> B ---------> D ---------> E")
    print("|            |            |            ^")
    print("|            |            v            |")
    print("|(5)         └-----(1)---> C -----(2)-┘")
    print("└--------------------------┘")
    
    # Display currently confirmed paths
    if prev:
        connections = []
        for node in visited:
            if prev.get(node):
                connections.append(f"{prev[node]} → {node}")
        
        if connections:
            print(f"\nConfirmed paths: {', '.join(connections)}")
        
        if current_node:
            print(f"Current: {current_node}")

def print_dijkstra_table(nodes, dist, visited, current_node, prev):
    """Print Dijkstra algorithm status table"""
    print("┌" + "─" * 8 + "┬" + "─" * 8 + "┬" + "─" * 12 + "┬" + "─" * 8 + "┐")
    print(f"│{'Status':<8}│{'Vertex':<8}│{'Prev Vertex':<12}│{'Weight':<8}│")
    print("├" + "─" * 8 + "┼" + "─" * 8 + "┼" + "─" * 12 + "┼" + "─" * 8 + "┤")
    
    for node in sorted(nodes):
        # Determine status
        if node in visited:
            status = "✓"
        elif node == current_node:
            status = "→"
        else:
            status = ""
        
        # Get predecessor node
        prev_str = "-" if prev is None or prev.get(node) is None else str(prev.get(node))
        
        # Get distance
        dist_str = "∞" if dist[node] == float('inf') else str(dist[node])
        
        print(f"│{status:<8}│{node:<8}│{prev_str:<12}│{dist_str:<8}│")
    
    print("└" + "─" * 8 + "┴" + "─" * 8 + "┴" + "─" * 12 + "┴" + "─" * 8 + "┘")

def print_graph_structure(graph):
    """Print graph structure visualization"""
    print("\n" + "="*50)
    print("Graph Structure Visualization")
    print("="*50)
    
    print("""
        (10)        (4)        (3)
A ---------> B ---------> D ---------> E
|            |            |            ^
|            |            v            |
|(5)         └-----(1)---> C -----(2)-┘
└--------------------------┘
    """)
    
    print("Adjacency list representation:")
    for source in sorted(graph.keys()):
        if graph[source]:
            connections = []
            for dest, weight in graph[source].items():
                connections.append(f"{dest}({weight})")
            print(f"  {source} → {', '.join(connections)}")
        else:
            print(f"  {source} → (no outgoing edges)")

def print_path_visualization(path, dist):
    """Visualize shortest path"""
    if not path:
        return
    
    print(f"\nShortest Path Visualization (Total Distance: {dist}):")
    print("="*40)
    
    # Simple arrow path display
    path_str = " → ".join(path)
    print(f"Path: {path_str}")
    
    # If path is known, display specific graphics
    if len(path) >= 2:
        print("\nPath Graphics:")
        for i in range(len(path) - 1):
            current = path[i]
            next_node = path[i + 1]
            print(f"  {current} =====> {next_node}")
            if i < len(path) - 2:
                print("    |")
                print("    v")

def print_final_diagram_and_table(dist, prev, start, graph):
    """Display final complete diagram and connections"""
    nodes = get_all_nodes(graph)
    
    print(f"\nFinal Result")
    print("=" * 40)
    
    # Final table
    print_dijkstra_table(nodes, dist, set(nodes), None, prev)
    
    # Display complete graph and paths
    print(f"\nComplete Graph with Shortest Paths from {start}:")
    print_cli_graph(set(nodes), None, prev)
    
    # Display distance summary
    print(f"\nDistances from {start}:")
    for node in sorted(nodes):
        dist_str = "∞" if dist[node] == float('inf') else str(dist[node])
        print(f"  {start} → {node}: {dist_str}")

def main():
    # Load graph data from CSV file
    graph = load_graph_from_csv(DATA_PATH)
    
    print("=== Dijkstra Shortest Path Algorithm ===")
    
    # Display graph structure
    print_graph_structure(graph)
    
    # Get user input for start and end points
    start, end = get_user_input(graph)
    
    if start == end:
        print(f"\nStart and end points are the same, distance is 0")
        print(f"Path: {start}")
        return
    
    # Run visualization algorithm directly
    print("\nStarting Dijkstra algorithm execution...")
    dist, prev = dijkstra_with_visualization(graph, start)
    
    path = reconstruct_path(prev, start, end)
    
    print(f"\n=== Results for Target Path ===")
    if dist[end] == float('inf'):
        print(f"No reachable path from {start} to {end}")
    else:
        print(f"Shortest distance from {start} to {end}: {dist[end]}")
        if path:
            print(f"Shortest path: {' → '.join(path)}")
            # Display path visualization
            print_path_visualization(path, dist[end])
        else:
            print("Unable to construct path")

if __name__ == "__main__":
    main()
