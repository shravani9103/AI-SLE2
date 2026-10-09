"""Convert a searched traffic-state path into a signal action."""

ACTION_BY_STATE = {
    "S0": "Prepare North-South priority",
    "S1": "Keep North-South green",
    "S2": "Balance phase timing",
    "S3": "Switch to East-West green",
    "S4": "Maintain optimized phase",
}


def build_action(path):
    if not path:
        return "No valid signal action"
    return ACTION_BY_STATE.get(path[-1], "Apply selected transition path")
