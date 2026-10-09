import cProfile
from traffic_graph import TRAFFIC_GRAPH, START_STATE, GOAL_STATE
from dfs_search import dfs


def workload():
    for _ in range(50000):
        dfs(TRAFFIC_GRAPH, START_STATE, GOAL_STATE)


if __name__ == "__main__":
    cProfile.run("workload()", "profiling/dfs.prof")
    print("Created profiling/dfs.prof")
