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

## Profiling Method

The following methods were used for profiling:

- **Execution Time:** Python `timeit` module
- **Node Measurement:** Manual node counting
- **Number of Profiling Executions:** 1,000

The same graph, start node, and goal node were used for both algorithms to make the comparison fair.

## Results

| Metric | BFS | DFS |
|---|---:|---:|
| Average Time | 0.011309 ms | 0.013244 ms |
| Nodes Expanded | 30 | 30 |
| Path Found | A → C → G → O → AD | A → C → G → O → AD |

## Observation

For the selected graph, BFS recorded a lower measured execution time than DFS.

Both BFS and DFS expanded the same number of nodes, i.e. 30 nodes.

The result is specific to the selected graph and search conditions.

## Justification and Analysis

The profiling results show that BFS had an average execution time of 0.011309 ms, while DFS had an average execution time of 0.013244 ms.

Both algorithms expanded 30 nodes and found the same path from A to AD.

Therefore, for this particular experiment, BFS recorded the lower measured execution time.

The result may change if the graph structure, node ordering, or goal position is changed.

This demonstrates why empirical profiling is useful for understanding the practical performance of algorithms.

## Technologies Used

- Python
- Python `timeit`
- Breadth-First Search
- Depth-First Search
- GitHub
- Visual Studio Code

## Project Files

| File | Description |
|---|---|
| `sle2.py` | BFS and DFS profiling program |
| `SLE2_26UAM307_Shravani Bramhadande.pdf` | SLE-2 profiling report |
| `README.md` | Project and experiment documentation |

## AI Contribution

ChatGPT was used to understand the SLE-2 requirements, prepare and explain the BFS and DFS profiling code, explain the profiling method, and organize the report.

The program was executed by the student, and the profiling results were verified and used for the final analysis.

## Conclusion

This experiment helped demonstrate how profiling can be used to compare search algorithms using actual performance data.

BFS and DFS were tested on the same graph using execution time and nodes expanded as performance measures.

For the selected graph, BFS recorded a lower measured execution time, while both algorithms expanded the same number of nodes.
