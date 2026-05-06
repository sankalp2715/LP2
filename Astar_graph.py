# A* Algorithm with user input

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': []
}

heuristic = {
    'A': 3,
    'B': 1,
    'C': 1,
    'D': 0
}

def Astar(start, goal):
    open_list = [start]
    cost = {start: 0}
    parent = {start: None}

    while open_list:
        # 🔹 pick node with lowest f(n) = g(n) + h(n)
        current = min(open_list, key=lambda n: cost[n] + heuristic[n])
        open_list.remove(current)

        if current == goal:
            # 🔹 reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("Path:", " → ".join(path))
            print("Total Cost:", cost[path[-1]])
            return

        # 🔹 expand neighbors
        for neighbour, weight in graph[current]:
            new_cost = cost[current] + weight
            if neighbour not in cost or new_cost < cost[neighbour]:
                cost[neighbour] = new_cost
                parent[neighbour] = current
                if neighbour not in open_list:
                    open_list.append(neighbour)

    print("No path found")


# 🔹 Take input from user
start = input("Enter start node (A/B/C/D): ").strip().upper()
goal = input("Enter goal node (A/B/C/D): ").strip().upper()

# 🔹 basic validation
if start not in graph or goal not in graph:
    print("Invalid nodes. Use only A, B, C, D.")
else:
    Astar(start, goal)