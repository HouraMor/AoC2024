def calculate_scores(file_path):

    with open(file_path, 'r') as f:
        grid = [list(map(int, line.strip())) for line in f.readlines()]

    rows = len(grid)
    cols = len(grid[0])

    def find_heads_and_ends(grid):
        trailheads = []
        trailends = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    trailheads.append((i, j))
                if grid[i][j] == 9:
                    trailends.append((i, j))
        return trailheads, trailends

    def is_valid_move(curr, next_pos):

        x, y = next_pos
        return (
            0 <= x < rows and 0 <= y < cols  # within bounds
            and grid[x][y] == grid[curr[0]][curr[1]] + 1  # exactly one step higher
        )

    def bfs(start):
        #bfs to find all reachable trailends from a trailhead
        queue = [start]
        visited = set()
        reachable_nines = []

        while queue:
            x, y = queue.pop(0)
            visited.add((x, y))

            if grid[x][y] == 9:
                reachable_nines.append((x, y))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_pos = (x + dx, y + dy)
                if  is_valid_move((x, y), next_pos):
                    queue.append(next_pos)
                    #visited.add(next_pos)

        return len(reachable_nines)

    # Identify trailheads and trailends
    trailheads, trailends = find_heads_and_ends(grid)

    # Calculate scores for each trailhead
    scores = [bfs(head) for head in trailheads]

    return scores


file_path = 'input.txt'
result = sum(calculate_scores(file_path))
print(f"Total scores: {result}")
