# AI-Algorithms

readme_content = """

## Key Concepts:
- **Objective**: Implement various AI search algorithms to find the best path from a start node (S) to a goal node (G).
- **Customization**: The graph and heuristic values are user-defined and can be adjusted for any specific problem.

## Search Algorithms and Expected Outputs

### 1. **British Museum Search**
   - **Description**: Brute-force approach; explores all possible paths exhaustively.
   - **Use Case**: Good for completeness but inefficient in large graphs.
   - **Expected Output**: Finds the goal by evaluating all possible paths.

### 2. **Depth-First Search (DFS)**
   - **Description**: Explores a branch as deeply as possible before backtracking.
   - **Use Case**: Works well for problems with deep solutions, but may not find the shortest path.
   - **Expected Output**: A path to the goal (not guaranteed to be the shortest).

### 3. **Breadth-First Search (BFS)**
   - **Description**: Explores nodes level by level, ensuring the shortest path in unweighted graphs.
   - **Use Case**: Best for unweighted graphs or problems where the shortest path is required.
   - **Expected Output**: Shortest path to the goal.

### 4. **Hill Climbing**
   - **Description**: A greedy algorithm that always expands the node with the lowest heuristic value.
   - **Use Case**: Fast but prone to local minima; does not guarantee an optimal solution.
   - **Expected Output**: A local optimum based on the heuristic values.

### 5. **Beam Search**
   - **Description**: Keeps track of a limited number of best nodes at each level to reduce memory usage.
   - **Use Case**: Useful when memory is a constraint and a heuristic is available.
   - **Expected Output**: A path, though not necessarily optimal due to memory limitations.

### 6. **Oracle Search**
   - **Description**: A hypothetical search algorithm that has perfect knowledge of the optimal path.
   - **Use Case**: Useful for comparison purposes or in environments with full path knowledge.
   - **Expected Output**: The shortest or optimal path to the goal.

### 7. **Branch and Bound (B&B)**
   - **Description**: Explores all paths but prunes those that are costlier than the best path found so far.
   - **Use Case**: Useful when we want to guarantee an optimal solution but reduce unnecessary exploration.
   - **Expected Output**: Optimal path with efficient pruning.

### 8. **Branch and Bound Greedy**
   - **Description**: Greedy version of B&B, using heuristics to guide the search.
   - **Use Case**: Faster than regular B&B but can miss the optimal path due to the greedy nature.
   - **Expected Output**: A heuristic-based path, potentially suboptimal.

### 9. **Branch and Bound Greedy with Dead Horse Principle**
   - **Description**: A variant of Greedy B&B that exits immediately when the goal node is found.
   - **Use Case**: Ideal when finding any solution quickly is more important than finding the optimal one.
   - **Expected Output**: First valid path to the goal.

### 10. **Branch and Bound Greedy with Heuristics**
   - **Description**: Combines cost and heuristic values for more aggressive pruning.
   - **Use Case**: Best when both cost and heuristic estimates are available for informed decisions.
   - **Expected Output**: More efficiently pruned path than regular B&B Greedy.

### 11. **A* Algorithm**
   - **Description**: Informed search using both path cost (g-value) and heuristics (h-value) to find the optimal path.
   - **Use Case**: Most commonly used algorithm for optimal pathfinding in graphs.
   - **Expected Output**: The optimal path with respect to both cost and heuristics.
