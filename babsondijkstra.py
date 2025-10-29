import heapq

# Node names = building names
# Edge weights = distance between buildings in feet
graph = {
    "Mandell Family Hall": {"Weissman Foundry": 125, "Coleman Hall": 700},
    "Weissman Foundry": {"Mandell Family Hall": 125, "Trim Dining Hall": 300, "Reynolds Campus Center": 125},
    "Trim Dining Hall": {"Weissman Foundry": 300, "Hollister Hall": 125, "Reynolds Campus Center": 400},
    "Sorensen Theater": {"Reynolds Campus Center": 50, "Horn Library": 300, "Glavin Chapel": 125, "The Globe": 100},
    "Horn Library": {"Sorensen Theater": 300, "Park Manor West": 250, "LGRAC": 400, "Olin Hall": 350},
    "Glavin Chapel": {"Sorensen Theater": 125, "Horn Library": 125, "Reynolds Campus Center": 125},
    "Reynolds Campus Center": {"Hollister Hall": 125, "Sorensen Theater": 50, "Weissman Foundry": 125, "Trim Dining Hall": 400},
    "Hollister Hall": {"Trim Dining Hall": 125, "Reynolds Campus Center": 125},
    "Van Winkle Hall": {"Coleman Hall": 100, "Upper Fields": 550},
    "Upper Fields": {"Van Winkle Hall": 550, "LGRAC": 625},
    "Coleman Hall": {"Mandell Family Hall": 700, "Van Winkle Hall": 100},
    "Park Manor West": {"Horn Library": 250, "Olin Hall": 350},
    "The Globe": {"Sorensen Theater": 100},
    "LGRAC": {"Horn Library": 400, "Upper Fields": 625, "Malloy Hall": 100},
    "Malloy Hall": {"LGRAC": 100, "Olin Hall": 110},
    "Olin Hall": {"Malloy Hall": 110, "Horn Library": 350, "Park Manor West": 350}
}


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # priority queue
    pq = [(0, start)]
    previous = {node: None for node in graph}
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, previous