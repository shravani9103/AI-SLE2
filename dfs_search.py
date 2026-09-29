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
    "P": [], "Q": [], "R": [], "S": [],
    "T": [], "U": [], "V": [], "W": [],
    "X": [], "Y": [], "Z": [],
    "AA": [], "AB": [], "AC": [], "AD": []
}

start = "A"
goal = "AD"


def dfs():
    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path

        for neighbor in reversed(graph[current]):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None


# Repeat enough times so py-spy can sample the program
for _ in range(200000):
    dfs()

path = dfs()

print("DFS Profiling")
print("Start:", start)
print("Goal:", goal)
print("Path:", " -> ".join(path))
print("Completed 200000 DFS runs")