"""Traffic-state graph used by the Traffic Signal Optimizer Agent."""

TRAFFIC_GRAPH = {
    "S0": ["S1", "S2"],
    "S1": ["S3", "S4"],
    "S2": ["S3"],
    "S3": ["S4"],
    "S4": [],
}

STATE_DESCRIPTION = {
    "S0": "High North-South queue",
    "S1": "North-South green phase",
    "S2": "Balanced traffic state",
    "S3": "East-West green phase",
    "S4": "Reduced congestion / goal state",
}

START_STATE = "S0"
GOAL_STATE = "S4"
