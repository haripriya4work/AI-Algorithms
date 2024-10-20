import matplotlib.pyplot as plt
import networkx as nx

def beam_search_visual(graph, start_node, goal_node, heuristic, beam_width):
    visited = set()
    queue = [start_node]
    level = 0
    
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(8, 6))
    
    while queue:
        visited.update(queue)

        draw_graph(graph, visited, pos, level, queue)

        if goal_node in queue:
            print(f"Goal node {goal_node} found at level {level}")
            break
        
        next_level_nodes = []
        for node in queue:
            next_level_nodes.extend([neighbor for neighbor in graph[node] if neighbor not in visited])

        if not next_level_nodes:
            print("No more nodes to expand, stopping.")
            break
        
        next_level_nodes = sorted(next_level_nodes, key = lambda node: heuristic[node])[:beam_width]

        queue = next_level_nodes
        level += 1  
    if goal_node not in visited:
        print("Goal node not found!")

    plt.show()

def draw_graph(graph, visited, pos, level, current_nodes):
    plt.clf()
    nx.draw(graph, pos, with_labels = True, node_color = 'lightgray', node_size = 500, font_size = 10, font_weight = 'bold', edge_color = 'gray')
    nx.draw_networkx_nodes(graph, pos, nodelist = list(visited), node_color = 'lightblue', node_size = 700)
    nx.draw_networkx_nodes(graph, pos, nodelist = current_nodes, node_color = 'orange', node_size = 700)
    plt.title(f"Beam Search - Level {level} (Beam Width: {len(current_nodes)})")
    plt.pause(1)

graph = nx.Graph()
graph.add_weighted_edges_from([('A', 'B', 2), ('A', 'C', 4), ('B', 'D', 3), ('B', 'E', 6), ('C', 'F', 5), ('C', 'G', 2), ('D', 'H', 4), ('E', 'I', 3), ('F', 'J', 2), ('G', 'K', 7)])

heuristic = {'A': 5, 'B': 3, 'C': 4, 'D': 27, 'E': 9, 'F': 1, 'G': 22, 'H': 5, 'I': 2, 'J': 0, 'K': 11}

start_node = 'A'
goal_node = 'G'

beam_width = 2
beam_search_visual(graph, start_node, goal_node, heuristic, beam_width)

plt.show()