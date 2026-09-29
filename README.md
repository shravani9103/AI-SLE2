 # SLE-2: BFS vs DFS Profiling

## Student Details

- **Course:** 02AML204 – Introduction to Artificial Intelligence
- **PRN:** 26UAM307
- **Name:** Shravani Sadashiv Bramhadande
- **Division:** A
- **Date:** 22-09-2026

## Objective

The objective of this SLE-2 experiment is to perform empirical performance analysis of two uninformed search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

Both algorithms were tested on the same graph to compare their practical performance.

## Problem Used

- **Problem:** Small graph search
- **Start Node:** A
- **Goal Node:** AD

Both BFS and DFS search for a path from node A to node AD.

## Algorithms Used

### Breadth-First Search (BFS)

BFS explores the graph level by level. It uses a queue to store nodes that are yet to be explored.

### Depth-First Search (DFS)

DFS explores a branch of the graph as deeply as possible before backtracking. It uses a stack to store nodes that are yet to be explored.

## Profiling Method

The following methods were used for profiling:

- **Execution Time:** Python `timeit` module
- **Node Measurement:** Manual node counting
- **Profiler:** `py-spy`
- **Profiling Runs:** 1,000 runs for time measurement
- **Additional Profiling:** 200,000 BFS/DFS runs for `py-spy` flamegraph generation

The same graph, start node, and goal node were used for both algorithms.

## Results

| Metric | BFS | DFS |
|---|---:|---:|
| Average Time | 0.011309 ms | 0.013244 ms |
| Nodes Expanded | 30 | 30 |
| Path Found | A → C → G → O → AD | A → C → G → O → AD |

## Observation

For the selected graph, BFS recorded a lower measured execution time than DFS.

Both BFS and DFS expanded the same number of nodes, i.e. 30 nodes.

Both algorithms found the same path:

`A → C → G → O → AD`

The result is specific to the selected graph and search conditions.

## py-spy Profiling

`py-spy` was used to generate flamegraphs for both search algorithms.

The profiling commands used were:

```text
py-spy record -o bfs_search.svg -- python bfs_search.py
py-spy record -o dfs_search.svg -- python dfs_search.py