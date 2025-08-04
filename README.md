This project simulates robot navigation on a 2D grid using two heuristic search algorithms: Best-First Search and A* Search. Users input the grid size, start and goal positions, and obstacle locations to create a custom environment. The robot must find a path from the start to the goal while avoiding obstacles.

Best-First Search selects the next step based only on the estimated distance to the goal (heuristic), making it fast but not always optimal. In contrast, A* uses both the actual cost from the start and the estimated cost to the goal, ensuring the shortest possible path if the heuristic is admissible.

The program uses Manhattan distance as the heuristic and implements priority queues for efficient path selection. The grid is displayed with symbols showing the path, start, goal, and obstacles, helping visualize how each algorithm navigates. This project highlights how intelligent pathfinding helps robots move efficiently through complex environments.
