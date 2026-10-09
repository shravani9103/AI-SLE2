from traffic_graph import TRAFFIC_GRAPH, START_STATE, GOAL_STATE
from dfs_search import dfs

for _ in range(1000000):
    dfs(TRAFFIC_GRAPH, START_STATE, GOAL_STATE)
