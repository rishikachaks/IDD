from babsondijkstra import graph, dijkstra

def print_shortest_path(graph, start, end):
    distances, previous = dijkstra(graph, start)
    
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous[current]
    
    print(f"Shortest path from {start} to {end}: {' → '.join(path)}")
    print(f"Total distance: {distances[end]} feet\n")
    print(f"Total time: {distances[end] / 186} minutes\n") # the average person can walk 186 feet in one minute

if __name__ == "__main__":
    # Example test cases

    # test case 1: my dorm to Olin Hall
    print_shortest_path(graph, "Mandell Family Hall", "Olin Hall")
    # test case 2: sorenson theater to horn library
    print_shortest_path(graph, "Sorensen Theater", "Horn Library")
    # test case 3: Park Manor West to the upper fields
    print_shortest_path(graph, "Park Manor West", "Upper Fields")
