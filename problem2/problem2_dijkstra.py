'''
CSC2103 Data Structures and Algorithms
Problem 2: Dijkstra's Algorithm Visualization
Author: Tan Kok Feng / Ch'ng Shen Ming


This program implements Dijkstra's algorithm with step-by-step visualization
to demonstrate how the algorithm finds the shortest path in a graph.
It includes a custom Min Heap implementation for priority queue functionality,
loads graph data from a CSV file, and provides an interactive command-line interface
for users to explore the algorithm's behavior.
'''

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

def display_menu():
    """Display interactive menu options"""
    print("\n" + "=" * 70)
    print("DIJKSTRA SHORTEST PATH ALGORITHM - Interactive Demo")
    print("=" * 70)
    print("🗺️  Find the shortest path between any two nodes in the graph")
    print("⚡ Features: Step-by-step visualization, algorithm demonstration")
    print("=" * 70)
    print("📊 GRAPH OPERATIONS:")
    print("1.  View graph structure")
    print("2.  Show graph from CSV data")
    print("")
    print("🛣️  PATH FINDING:")
    print("3.  Find shortest path (with visualization)")
    print("4.  Find shortest path (quick mode)")
    print("5.  Compare all paths from a node")
    print("")
    print("🔍 GRAPH ANALYSIS:")
    print("6.  Display adjacency list")
    print("7.  Show all possible connections")
    print("8.  Graph statistics")
    print("")
    print("🧪 DEMONSTRATION & UTILITIES:")
    print("9.  Run algorithm step-by-step demo")
    print("10. Show example scenarios")
    print("11. Load custom graph data")
    print("0.  Exit program")
    print("=" * 70)

def ask_continue_choice(additional_options=None):
    """Unified continue choice function for better code reusability"""
    print("\n" + "=" * 50)
    print("Do you want to continue?")
    
    options = {}
    option_num = 1
    
    # Add additional options if provided
    if additional_options:
        for option in additional_options:
            print(f"{option_num}. {option}")
            options[str(option_num)] = f"option_{option_num}"
            option_num += 1
    
    # Add standard options
    print(f"{option_num}. Back to main menu")
    options[str(option_num)] = "home"
    option_num += 1
    
    print(f"{option_num}. Exit")
    options[str(option_num)] = "exit"
    
    while True:
        try:
            choice = input(f"\nEnter your choice (1-{len(options)}): ").strip()
            
            if choice in options:
                if options[choice] == "home":
                    return "home"
                elif options[choice] == "exit":
                    print("👋 Thank you for using our Dijkstra algorithm program!")
                    exit()
                else:
                    return options[choice]
            else:
                print(f"❌ Invalid choice. Please enter a number between 1 and {len(options)}.")
        except KeyboardInterrupt:
            print("\n❌ Operation cancelled. Returning to main menu...")
            return "home"

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
    """
    Main program function with interactive menu
    Demonstrates Dijkstra algorithm with comprehensive user experience
    """
    print("Dijkstra Algorithm Implementation - CSC2103 Data Structures Assignment")
    print("This program demonstrates the Dijkstra shortest path algorithm")
    print("with step-by-step visualization and comprehensive graph analysis.")
    
    # Load graph data from CSV file
    try:
        graph = load_graph_from_csv(DATA_PATH)
        print(f"✅ Successfully loaded graph from {DATA_PATH}")
    except FileNotFoundError:
        print(f"❌ Error: Could not find graph data file at {DATA_PATH}")
        print("Please ensure the graph_edges.csv file exists.")
        return
    except Exception as e:
        print(f"❌ Error loading graph data: {e}")
        return

    while True:
        display_menu()

        try:
            choice = input("\nEnter your choice (0-11): ").strip()

            if choice == '0':
                print("👋 Thank you for using our Dijkstra algorithm program!")
                break

            elif choice == '1':
                print("\n🗺️  GRAPH STRUCTURE VISUALIZATION")
                print_graph_structure(graph)
                ask_continue_choice()

            elif choice == '2':
                print("\n📊 GRAPH DATA FROM CSV")
                print("=" * 50)
                print(f"Data source: {DATA_PATH}")
                print("=" * 50)
                
                # Display CSV data in table format
                try:
                    with open(DATA_PATH, 'r', encoding='utf-8') as file:
                        reader = csv.DictReader(file)
                        print("┌" + "─" * 10 + "┬" + "─" * 13 + "┬" + "─" * 8 + "┐")
                        print(f"│{'Source':<10}│{'Destination':<13}│{'Weight':<8}│")
                        print("├" + "─" * 10 + "┼" + "─" * 13 + "┼" + "─" * 8 + "┤")
                        
                        for row in reader:
                            print(f"│{row['source']:<10}│{row['destination']:<13}│{row['weight']:<8}│")
                        
                        print("└" + "─" * 10 + "┴" + "─" * 13 + "┴" + "─" * 8 + "┘")
                
                except Exception as e:
                    print(f"Error reading CSV file: {e}")
                
                ask_continue_choice()

            elif choice == '3':
                print("\n🛣️  SHORTEST PATH WITH VISUALIZATION")
                nodes = get_all_nodes(graph)
                print(f"Available nodes: {', '.join(nodes)}")
                print("This mode will show step-by-step algorithm execution.")
                
                start, end = get_user_input(graph)
                
                if start == end:
                    print(f"\n✅ Start and end points are the same!")
                    print(f"Distance: 0")
                    print(f"Path: {start}")
                    ask_continue_choice()
                    continue
                
                print(f"\n🚀 Starting Dijkstra algorithm from {start} to {end}...")
                input("Press Enter to begin step-by-step execution...")
                
                dist, prev = dijkstra_with_visualization(graph, start)
                path = reconstruct_path(prev, start, end)
                
                print(f"\n🎯 FINAL RESULTS")
                if dist[end] == float('inf'):
                    print(f"❌ No reachable path from {start} to {end}")
                else:
                    print(f"✅ Shortest distance from {start} to {end}: {dist[end]}")
                    if path:
                        print(f"🛣️  Shortest path: {' → '.join(path)}")
                        print_path_visualization(path, dist[end])
                
                choice_result = ask_continue_choice(["Find another path"])
                if choice_result == "option_1":
                    continue

            elif choice == '4':
                print("\n⚡ QUICK PATH FINDING")
                nodes = get_all_nodes(graph)
                print(f"Available nodes: {', '.join(nodes)}")
                print("This mode provides instant results without step-by-step visualization.")
                
                start, end = get_user_input(graph)
                
                if start == end:
                    print(f"\n✅ Start and end points are the same!")
                    print(f"Distance: 0, Path: {start}")
                    ask_continue_choice()
                    continue
                
                print(f"\n🔄 Computing shortest path from {start} to {end}...")
                dist, prev = dijkstra(graph, start)
                path = reconstruct_path(prev, start, end)
                
                print(f"\n🎯 RESULTS:")
                if dist[end] == float('inf'):
                    print(f"❌ No reachable path from {start} to {end}")
                else:
                    print(f"✅ Shortest distance: {dist[end]}")
                    if path:
                        print(f"🛣️  Path: {' → '.join(path)}")
                        print_path_visualization(path, dist[end])
                
                choice_result = ask_continue_choice(["Find another path"])
                if choice_result == "option_1":
                    continue

            elif choice == '5':
                print("\n🌐 COMPARE ALL PATHS FROM A NODE")
                nodes = get_all_nodes(graph)
                print(f"Available nodes: {', '.join(nodes)}")
                
                while True:
                    start = input("Enter starting node: ").strip().upper()
                    if start in nodes:
                        break
                    print(f"❌ Node '{start}' does not exist. Please choose from: {', '.join(nodes)}")
                
                print(f"\n🔄 Computing all shortest paths from {start}...")
                dist, prev = dijkstra(graph, start)
                
                print(f"\n📊 ALL DISTANCES FROM {start}:")
                print("=" * 40)
                for node in sorted(nodes):
                    if node == start:
                        continue
                    
                    dist_str = "∞" if dist[node] == float('inf') else str(dist[node])
                    path = reconstruct_path(prev, start, node)
                    path_str = ' → '.join(path) if path and path[0] == start else "No path"
                    
                    print(f"{start} → {node}: Distance {dist_str}")
                    if path and path[0] == start:
                        print(f"    Path: {path_str}")
                    print()
                
                ask_continue_choice()

            elif choice == '6':
                print("\n📋 ADJACENCY LIST REPRESENTATION")
                print("=" * 50)
                
                nodes = get_all_nodes(graph)
                for source in sorted(nodes):
                    if graph.get(source, {}):
                        connections = []
                        for dest, weight in graph[source].items():
                            connections.append(f"{dest}(weight:{weight})")
                        print(f"📍 {source} → {', '.join(connections)}")
                    else:
                        print(f"📍 {source} → (no outgoing edges)")
                
                ask_continue_choice()

            elif choice == '7':
                print("\n🔗 ALL POSSIBLE CONNECTIONS")
                print("=" * 50)
                
                total_edges = 0
                all_connections = []
                
                for source in graph:
                    for dest, weight in graph[source].items():
                        all_connections.append((source, dest, weight))
                        total_edges += 1
                
                print(f"Total edges: {total_edges}")
                print("┌" + "─" * 12 + "┬" + "─" * 15 + "┬" + "─" * 8 + "┐")
                print(f"│{'From':<12}│{'To':<15}│{'Weight':<8}│")
                print("├" + "─" * 12 + "┼" + "─" * 15 + "┼" + "─" * 8 + "┤")
                
                for source, dest, weight in sorted(all_connections):
                    print(f"│{source:<12}│{dest:<15}│{weight:<8}│")
                
                print("└" + "─" * 12 + "┴" + "─" * 15 + "┴" + "─" * 8 + "┘")
                
                ask_continue_choice()

            elif choice == '8':
                print("\n📈 GRAPH STATISTICS")
                print("=" * 50)
                
                nodes = get_all_nodes(graph)
                total_nodes = len(nodes)
                total_edges = sum(len(graph[node]) for node in graph)
                
                # Calculate average degree
                degrees = [len(graph.get(node, {})) for node in nodes]
                avg_degree = sum(degrees) / len(degrees) if degrees else 0
                
                print(f"📊 Basic Statistics:")
                print(f"  • Total nodes: {total_nodes}")
                print(f"  • Total edges: {total_edges}")
                print(f"  • Average out-degree: {avg_degree:.2f}")
                print(f"  • Graph density: {total_edges/(total_nodes*(total_nodes-1)):.3f}" if total_nodes > 1 else "  • Graph density: 0")
                
                print(f"\n🔢 Node Degrees:")
                for node in sorted(nodes):
                    out_degree = len(graph.get(node, {}))
                    print(f"  • {node}: {out_degree} outgoing edge(s)")
                
                ask_continue_choice()

            elif choice == '9':
                print("\n🧪 ALGORITHM STEP-BY-STEP DEMO")
                print("This demo will run the algorithm with predefined start/end points")
                print("to demonstrate how Dijkstra's algorithm works.")
                
                nodes = get_all_nodes(graph)
                demo_start = nodes[0] if nodes else 'A'
                demo_end = nodes[-1] if len(nodes) > 1 else nodes[0]
                
                print(f"\n📝 Demo: Finding path from {demo_start} to {demo_end}")
                input("Press Enter to start the demonstration...")
                
                dist, prev = dijkstra_with_visualization(graph, demo_start)
                path = reconstruct_path(prev, demo_start, demo_end)
                
                print(f"\n🎓 DEMO COMPLETED!")
                if path:
                    print(f"📚 Learned: Path from {demo_start} to {demo_end} = {' → '.join(path)} (distance: {dist[demo_end]})")
                
                ask_continue_choice()

            elif choice == '10':
                print("\n📖 EXAMPLE SCENARIOS")
                print("=" * 50)
                
                scenarios = [
                    ("Shortest path", "Find the most efficient route between two cities"),
                    ("Network routing", "Determine optimal data packet routes in networks"),
                    ("GPS navigation", "Calculate fastest route considering traffic"),
                    ("Cost optimization", "Minimize transportation costs between locations")
                ]
                
                print("🌟 Real-world applications of Dijkstra's algorithm:")
                for i, (title, description) in enumerate(scenarios, 1):
                    print(f"\n{i}. {title}:")
                    print(f"   {description}")
                
                print(f"\n💡 Try running the algorithm with different start/end points")
                print(f"   to see how the shortest path changes!")
                
                ask_continue_choice()

            elif choice == '11':
                print("\n📁 LOAD CUSTOM GRAPH DATA")
                print("=" * 50)
                print(f"Current data file: {DATA_PATH}")
                print(f"File format: CSV with columns 'source', 'destination', 'weight'")
                
                try:
                    # Reload the graph
                    graph = load_graph_from_csv(DATA_PATH)
                    nodes = get_all_nodes(graph)
                    print(f"\n✅ Graph reloaded successfully!")
                    print(f"📊 Loaded {len(nodes)} nodes with {sum(len(graph[node]) for node in graph)} edges")
                    print(f"🔗 Available nodes: {', '.join(nodes)}")
                    
                except Exception as e:
                    print(f"❌ Error reloading graph: {e}")
                
                ask_continue_choice()

            else:
                print("❌ Invalid choice. Please enter a number between 0 and 11.")

        except KeyboardInterrupt:
            print("\n\n⚠️  Program interrupted by user.")
            confirm = input("Do you want to exit? [y/N]: ").lower()
            if confirm == 'y':
                print("👋 Goodbye!")
                break
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            print("💡 Please try again or restart the program.")

if __name__ == "__main__":
    main()
