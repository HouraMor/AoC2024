def guard_path_optimized(file_path):

    with open(file_path, 'r') as f:
        map_lines = f.read().strip().splitlines()

    rows, cols = len(map_lines), len(map_lines[0])


    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    direction_order = ['^', '>', 'v', '<']
    visited = set()

    # starting position and direction
    start_row, start_col, direction = None, None, None
    for r in range(rows):
        for c in range(cols):
            if map_lines[r][c] in directions:
                start_row, start_col = r, c
                direction = map_lines[r][c]
                break
        if start_row is not None:
            break

    # Initialize guard's position and direction
    row, col = start_row, start_col
    direction_idx = direction_order.index(direction)
    visited.add((row, col))  # Mark starting position as visited


    while True:
        # the next position
        delta_row, delta_col = directions[direction_order[direction_idx]]
        next_row, next_col = row + delta_row, col + delta_col


        if not (0 <= next_row < rows and 0 <= next_col < cols):
            break

        # if the next position is an obstacle
        if map_lines[next_row][next_col] == '#':
            # Turn right
            direction_idx = (direction_idx + 1) % 4
        else:

            row, col = next_row, next_col
            visited.add((row, col))

    return len(visited)

file_path = 'input.txt'
result = guard_path_optimized(file_path)
print(result)
