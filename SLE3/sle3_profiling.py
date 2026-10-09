from timeit import default_timer
from traffic_graph import TRAFFIC_GRAPH, START_STATE, GOAL_STATE, STATE_DESCRIPTION
from bfs_search import bfs
from dfs_search import dfs

NUMBER_OF_RUNS = 10000


def benchmark(search_function):
    times = []
    path = None
    expanded = 0
    for _ in range(NUMBER_OF_RUNS):
        start = default_timer()
        path, expanded = search_function(TRAFFIC_GRAPH, START_STATE, GOAL_STATE)
        end = default_timer()
        times.append((end - start) * 1000)
    return sum(times) / len(times), path, expanded


def main():
    bfs_time, bfs_path, bfs_nodes = benchmark(bfs)
    dfs_time, dfs_path, dfs_nodes = benchmark(dfs)

    print("\n========================================")
    print("   SLE-3: TRAFFIC SIGNAL OPTIMIZER")
    print("========================================")
    print(f"Start state: {START_STATE} - {STATE_DESCRIPTION[START_STATE]}")
    print(f"Goal state : {GOAL_STATE} - {STATE_DESCRIPTION[GOAL_STATE]}")
    print(f"Runs       : {NUMBER_OF_RUNS}")
    print("\n---------- BFS ----------")
    print(f"Average Time: {bfs_time:.6f} ms")
    print(f"Nodes Expanded: {bfs_nodes}")
    print("Path Found:", " -> ".join(bfs_path or []))
    print("\n---------- DFS ----------")
    print(f"Average Time: {dfs_time:.6f} ms")
    print(f"Nodes Expanded: {dfs_nodes}")
    print("Path Found:", " -> ".join(dfs_path or []))
    print("\n---------- COMPARISON ----------")
    print("Lower execution time:", "BFS" if bfs_time < dfs_time else "DFS")
    if bfs_nodes < dfs_nodes:
        print("Fewer nodes expanded: BFS")
    elif dfs_nodes < bfs_nodes:
        print("Fewer nodes expanded: DFS")
    else:
        print("Both expanded the same number of states.")

    result_file = "results/results.txt"
    with open(result_file, "w", encoding="utf-8") as f:
        f.write("SLE-3 Traffic Signal Optimizer Agent — BFS vs DFS Performance\n")
        f.write("==============================================================\n")
        f.write(f"Start State: {START_STATE} ({STATE_DESCRIPTION[START_STATE]})\n")
        f.write(f"Goal State: {GOAL_STATE} ({STATE_DESCRIPTION[GOAL_STATE]})\n")
        f.write(f"Runs: {NUMBER_OF_RUNS}\n\n")
        f.write(f"BFS Average Time: {bfs_time:.6f} ms\n")
        f.write(f"BFS Nodes Expanded: {bfs_nodes}\n")
        f.write(f"BFS Path: {' -> '.join(bfs_path or [])}\n\n")
        f.write(f"DFS Average Time: {dfs_time:.6f} ms\n")
        f.write(f"DFS Nodes Expanded: {dfs_nodes}\n")
        f.write(f"DFS Path: {' -> '.join(dfs_path or [])}\n\n")
        f.write(f"Lower execution time: {'BFS' if bfs_time < dfs_time else 'DFS'}\n")
        f.write("Note: measured time varies by machine and Python runtime.\n")


if __name__ == "__main__":
    main()
