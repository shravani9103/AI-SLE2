from collections import deque


def bfs(graph, start, goal):
    """Return a shortest transition path and number of expanded states."""
    queue = deque([(start, [start])])
    visited = set()
    expanded = 0

    while queue:
        current, path = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        expanded += 1

        if current == goal:
            return path, expanded

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None, expanded
