from collections import deque
import timeit


def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    nodes_expanded = 0

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None, nodes_expanded


def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    nodes_expanded = 0

    while stack:
        current, path = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        for neighbor in reversed(graph[current]):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None, nodes_expanded


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H", "I"],
    "E": ["J", "K"],
    "F": ["L", "M"],
    "G": ["N", "O"],
    "H": ["P", "Q"],
    "I": ["R", "S"],
    "J": ["T", "U"],
    "K": ["V", "W"],
    "L": ["X", "Y"],
    "M": ["Z"],
    "N": ["AA", "AB"],
    "O": ["AC", "AD"],
    "P": [],
    "Q": [],
    "R": [],
    "S": [],
    "T": [],
    "U": [],
    "V": [],
    "W": [],
    "X": [],
    "Y": [],
    "Z": [],
    "AA": [],
    "AB": [],
    "AC": [],
    "AD": []
}


start_node = "A"
goal_node = "AD"
NUMBER_OF_RUNS = 1000


# ---------------- BFS PROFILING ----------------

bfs_times = []

for i in range(NUMBER_OF_RUNS):

    start_time = timeit.default_timer()

    bfs_path, bfs_nodes = bfs(
        graph,
        start_node,
        goal_node
    )

    end_time = timeit.default_timer()

    elapsed_time = (end_time - start_time) * 1000

    bfs_times.append(elapsed_time)


bfs_average = sum(bfs_times) / len(bfs_times)


# ---------------- DFS PROFILING ----------------

dfs_times = []

for i in range(NUMBER_OF_RUNS):

    start_time = timeit.default_timer()

    dfs_path, dfs_nodes = dfs(
        graph,
        start_node,
        goal_node
    )

    end_time = timeit.default_timer()

    elapsed_time = (end_time - start_time) * 1000

    dfs_times.append(elapsed_time)


dfs_average = sum(dfs_times) / len(dfs_times)


# ---------------- RESULTS ----------------

print("\n========================================")
print("       SLE-2: BFS vs DFS")
print("========================================")

print("\nProblem:")
print("Start Node :", start_node)
print("Goal Node  :", goal_node)

print("\nNumber of Profiling Runs:", NUMBER_OF_RUNS)


print("\n---------- BFS ----------")

print(f"Average Time: {bfs_average:.6f} ms")
print("Nodes Expanded:", bfs_nodes)
print("Path Found:", " -> ".join(bfs_path))


print("\n---------- DFS ----------")

print(f"Average Time: {dfs_average:.6f} ms")
print("Nodes Expanded:", dfs_nodes)
print("Path Found:", " -> ".join(dfs_path))


print("\n========================================")
print("             COMPARISON")
print("========================================")


if bfs_average < dfs_average:
    print("Lower execution time: BFS")
else:
    print("Lower execution time: DFS")


if bfs_nodes < dfs_nodes:
    print("Fewer nodes expanded: BFS")

elif dfs_nodes < bfs_nodes:
    print("Fewer nodes expanded: DFS")

else:
    print("Both expanded the same number of nodes.")