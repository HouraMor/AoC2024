import string

def calculate_count_of_antinodes(file_path):
    # Read the map from the file
    with open(file_path, 'r') as f:

        grid = [line.strip() for line in f.readlines()]

    rows = len(grid)
    cols = len(grid[0])

    def componentwise_distance(point1, point2):
        return tuple((a - b) for a, b in zip(point1, point2))

    def is_position_valid(pos):
        return (0 <= pos[0] < rows and 0 <= pos[1] < cols)

    def find_allowed_positions(grid, allowed_chars):
        positions_dict = {char: [] for char in allowed_chars}  # Initialize dictionary with empty lists for each allowed char

        # Iterate through each row and column
        for row_index, row in enumerate(grid):
            for col_index, char in enumerate(row):
                if char in allowed_chars:
                    positions_dict[char].append((row_index, col_index))  # Add the position to the corresponding character's list

        return positions_dict

    # List of allowed characters for antennas
    allowed_characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)

    # Find all antenna positions in the grid
    positions_dict = find_allowed_positions(grid, allowed_characters)

    antinodes = set()

    # For each character with more than one antenna, find the antinode positions
    for char, positions in positions_dict.items():
        if len(positions) < 2:
            continue  # Skip characters with less than two antennas

        # Compare each pair of antennas with the same character
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                pos1 = positions[i]
                pos2 = positions[j]
                antinodes.add(pos1)
                antinodes.add(pos2)
                # Calculate the distance between the two antennas
                distance = componentwise_distance(pos1, pos2)
                # Calculate the two antinode positions
                pos1_antinode = (pos1[0] + distance[0], pos1[1] + distance[1])
                pos2_antinode = (pos2[0] - distance[0], pos2[1] - distance[1])

                # Check if the antinode positions are valid and add them to the set
                while is_position_valid(pos1_antinode):
                    antinodes.add(pos1_antinode)
                    pos1_antinode = (pos1_antinode[0] + distance[0], pos1_antinode[1] + distance[1])

                while is_position_valid(pos2_antinode):
                    antinodes.add(pos2_antinode)
                    pos2_antinode = (pos2_antinode[0] - distance[0], pos2_antinode[1] - distance[1])

    # Return the number of unique antinodes
    return len(antinodes)


file_path = 'input.txt'
result = calculate_count_of_antinodes(file_path)
print(f"Number of antinodes: {result}")
