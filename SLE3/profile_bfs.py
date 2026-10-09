import cProfile
from traffic_graph import TRAFFIC_GRAPH, START_STATE, GOAL_STATE
from bfs_search import bfs


def workload():
    for _ in range(50000):
        bfs(TRAFFIC_GRAPH, START_STATE, GOAL_STATE)


if __name__ == "__main__":
    cProfile.run("workload()", "profiling/bfs.prof")
    print("Created profiling/bfs.prof")
