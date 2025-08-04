import heapq

# Directions: Up, Down, Left, Right
directions = [(-1,0), (1,0), (0,-1), (0,1)]

def heuristic(a, b):
    # Manhattan Distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def is_valid(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != '#'

def reconstruct_path(came_from, end):
    path = []
    while end in came_from:
        path.append(end)
        end = came_from[end]
    path.reverse()
    return path

# --- Best-First Search ---
def best_first_search(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), start))
    came_from = {}
    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, goal)

        visited.add(current)

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            if is_valid(grid, neighbor[0], neighbor[1]) and neighbor not in visited:
                if neighbor not in [n for _, n in open_set]:
                    came_from[neighbor] = current
                    heapq.heappush(open_set, (heuristic(neighbor, goal), neighbor))

    return None

# --- A* Search ---
def a_star_search(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current_g, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, goal)

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            if not is_valid(grid, neighbor[0], neighbor[1]):
                continue

            temp_g_score = g_score[current] + 1

            if neighbor not in g_score or temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score = temp_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, temp_g_score, neighbor))

    return None

# --- Grid Representation ---
# '.' = empty space
# '#' = obstacle
# 'S' = start
# 'G' = goal

grid = [
    ['S', '.', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '#', '.'],
    ['.', '.', '#', '#', '.', '#', '.', '.'],
    ['#', '.', '.', '.', '.', '.', '.', 'G']
]

# Find start and goal positions
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            start = (i, j)
        if grid[i][j] == 'G':
            goal = (i, j)

# --- Run Both Algorithms ---
print("\n--- Best-First Search Path ---")
path_bfs = best_first_search(grid, start, goal)
if path_bfs:
    for r, c in path_bfs:
        if grid[r][c] == '.':
            grid[r][c] = 'B'
else:
    print("No path found using Best-First Search.")

# Show grid with BFS path
for row in grid:
    print(' '.join(row))

# Reset grid for A* path
grid = [
    ['S', '.', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '#', '.'],
    ['.', '.', '#', '#', '.', '#', '.', '.'],
    ['#', '.', '.', '.', '.', '.', '.', 'G']
]

print("\n--- A* Search Path ---")
path_astar = a_star_search(grid, start, goal)
if path_astar:
    for r, c in path_astar:
        if grid[r][c] == '.':
            grid[r][c] = 'A'
else:
    print("No path found using A* Search.")

# Show grid with A* path
for row in grid:
    print(' '.join(row))
