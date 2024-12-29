def find_obstruction_positions(file_path):

    with open(file_path, 'r') as f:
        map_lines = f.read().strip().splitlines()

    rows, cols = len(map_lines), len(map_lines[0])


    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    direction_order = ['^', '>', 'v', '<']


    start_row, start_col, direction = None, None, None
    for r in range(rows):
        for c in range(cols):
            if map_lines[r][c] in directions:
                start_row, start_col = r, c
                direction = map_lines[r][c]
                break
        if start_row is not None:
            break

    # Function to simulate guard movement and detect loops
    def causes_loop_with_obstruction(obstruction):
        visited = set()  # (row, col, direction)
        row, col, direction_idx = start_row, start_col, direction_order.index(direction)

        while True:
            # if we revisit a state, a loop exists
            state = (row, col, direction_idx)
            if state in visited:
                return True
            visited.add(state)

            # the next position
            delta_row, delta_col = directions[direction_order[direction_idx]]
            next_row, next_col = row + delta_row, col + delta_col


            if not (0 <= next_row < rows and 0 <= next_col < cols):
                break

            # if the next position is an obstacle (considering temporary obstruction)
            if (next_row, next_col) == obstruction or map_lines[next_row][next_col] == '#':

                direction_idx = (direction_idx + 1) % 4
            else:

                row, col = next_row, next_col

        return False

    # Test all open positions for possible obstructions
    possible_positions = []
    for r in range(rows):
        for c in range(cols):
            # Skip the starting position or existing obstacles
            if (r, c) == (start_row, start_col) or map_lines[r][c] == '#':
                continue


            if causes_loop_with_obstruction((r, c)):
                possible_positions.append((r, c))

    return len(possible_positions), possible_positions


file_path = "input.txt"
num_positions, obstruction_positions = find_obstruction_positions(file_path)
print(f"{num_positions} possible obstruction positions.")
print("Positions:", obstruction_positions)
