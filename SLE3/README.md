# SLE-3: Traffic Signal Optimizer Agent — BFS/DFS Performance Analysis

## Student Details

- **PRN:** 26UAM307
- **Name:** Shravani Sadashiv Bramhadande
- **System:** Traffic Signal Optimizer Agent

## Overview

This SLE-3 project extends the BFS/DFS search work from SLE-2 into a complete C4 architecture and a small executable prototype for a **Traffic Signal Optimizer Agent**.

The agent receives traffic-state information, builds a state graph, searches for a suitable state transition path using **BFS** or **DFS**, checks the goal state, and converts the selected path into a signal action.

## Project Objectives

1. Model traffic conditions as a state graph.
2. Implement BFS and DFS search for the traffic-state graph.
3. Compare BFS and DFS using execution time and nodes expanded.
4. Separate search, decision, and output responsibilities.
5. Represent the architecture using C4 Levels 1–4.
6. Keep the project folder structured for GitHub submission.

## Traffic Optimization Model

The prototype uses abstract traffic states such as:

- `S0` — high traffic on North-South road
- `S1` — North-South green phase
- `S2` — balanced traffic
- `S3` — East-West green phase
- `S4` — reduced congestion / target state

Each edge represents a possible signal transition. The goal is to reach the target traffic state with a valid sequence of transitions.

## Algorithms

### Breadth-First Search (BFS)
BFS explores states level by level using a queue. In an unweighted state graph it finds a path with the minimum number of transitions.

### Depth-First Search (DFS)
DFS explores one branch deeply before backtracking. It uses a stack and may find a valid path before BFS, but the path is not guaranteed to have the minimum number of transitions.

## Performance Analysis

Run:

```text
python sle3_profiling.py
```

The program performs repeated searches on the same traffic-state graph and records:

- average execution time
- nodes expanded
- path found
- lower-time algorithm
- fewer-node algorithm

Results are written to `results/results.txt`.

## cProfile

Run:

```text
python profile_bfs.py
python profile_dfs.py
```

The generated profiling data is stored in `profiling/bfs.prof` and `profiling/dfs.prof`.

`profiling/bfs_profile.svg` and `profiling/dfs_profile.svg` contain project-specific SVG profile summaries generated from the cProfile statistics.

## py-spy

The project also includes:

- `pyspy_bfs_target.py`
- `pyspy_dfs_target.py`

If py-spy is installed, flamegraphs can be generated with commands similar to:

```text
py-spy record --format flamegraph --output profiling/pyspy_bfs.svg -- python pyspy_bfs_target.py
py-spy record --format flamegraph --output profiling/pyspy_dfs.svg -- python pyspy_dfs_target.py
```

## C4 Architecture

### Level 1 — System Context
Shows the Traffic Signal Optimizer Agent and its interaction with the Traffic Operator, Traffic State, and Traffic Signal Environment.

### Level 2 — Container
Shows:

- Traffic Input
- Data Processor
- Search Engine
- Signal Decision
- Output Module

### Level 3 — Component
The Search Engine is divided into:

- Traffic State Graph
- BFS Search Module
- DFS Search Module
- Goal / State Checker
- Path / Action Builder

### Level 4 — Code
The code-level implementation is represented by:

- `traffic_graph.py`
- `bfs_search.py`
- `dfs_search.py`
- `signal_decision.py`
- `sle3_profiling.py`

## Folder Structure

```text
traffic-signal-optimizer-agent-main/
│
├── diagrams/
│   ├── C4-Context.puml
│   ├── C4-Container.puml
│   ├── C4-Component.puml
│   └── C4-Code.puml
│
├── out/diagrams/
│   ├── C4-Context/C4-Context.png
│   ├── C4-Container/C4-Container.png
│   ├── C4-Component/C4-Component.png
│   └── C4-Code/C4-Code.png
│
├── profiling/
│   ├── bfs.prof
│   ├── dfs.prof
│   ├── bfs_profile.svg
│   └── dfs_profile.svg
│
├── report 1/
│   └── SLE3_26UAM307_ShravaniBramhadande.docx
│
├── results/
│   └── results.txt
│
├── bfs_search.py
├── dfs_search.py
├── traffic_graph.py
├── signal_decision.py
├── sle3_profiling.py
├── profile_bfs.py
├── profile_dfs.py
├── pyspy_bfs_target.py
├── pyspy_dfs_target.py
├── CONTRIBUTION_LOG.md
└── README.md
```

## Conclusion

The SLE-3 project converts the BFS/DFS search idea into a Traffic Signal Optimizer Agent and documents the system using all four C4 levels. The same search algorithms remain reusable while traffic input, goal checking, signal decision, output, and performance analysis are separated into clear modules.
