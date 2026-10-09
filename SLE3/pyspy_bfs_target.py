from traffic_graph import TRAFFIC_GRAPH, START_STATE, GOAL_STATE
from bfs_search import bfs

for _ in range(1000000):
    bfs(TRAFFIC_GRAPH, START_STATE, GOAL_STATE)
