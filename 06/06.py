def guard_path(file_path):

    with open(file_path, 'r') as f:
        map_lines = f.read().strip().splitlines()

    rows, cols = len(map_lines), len(map_lines[0])

    # Directions: Up, Right, Down, Left
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

    # Mark the starting position as visited
    visited.add((start_row, start_col))


    def is_valid_position(row, col):
        return 0 <= row < rows and 0 <= col < cols and map_lines[row][col] != '#'

    row, col = start_row, start_col
    direction_idx = direction_order.index(direction)


    while True:
        # next position
        next_row, next_col = row + directions[direction_order[direction_idx]][0], col + directions[direction_order[direction_idx]][1]

        # If the next position is valid, move forward
        if is_valid_position(next_row, next_col):
            row, col = next_row, next_col
            visited.add((row, col))
        else:
            # if the guard would go out of bounds after turning
            if not (0 <= next_row < rows and 0 <= next_col < cols):
                break
            # If there's an obstacle, turn right (change direction)
            direction_idx = (direction_idx + 1) % 4
            next_row, next_col = row + directions[direction_order[direction_idx]][0], col + directions[direction_order[direction_idx]][1]



            # Move in the new direction
            row, col = next_row, next_col
            visited.add((row, col))

    return len(visited)


file_path = 'input.txt'
result = guard_path(file_path)
print(result)
