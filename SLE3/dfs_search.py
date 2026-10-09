def dfs(graph, start, goal):
    """Return a depth-first path and number of expanded states."""
    stack = [(start, [start])]
    visited = set()
    expanded = 0

    while stack:
        current, path = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        expanded += 1

        if current == goal:
            return path, expanded

        for neighbor in reversed(graph.get(current, [])):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None, expanded
