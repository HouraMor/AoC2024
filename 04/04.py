def count_xmas_occurrences_in_file(file_path):
    with open(file_path, 'r') as f:

        grid = [line.strip() for line in f.readlines()]

    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_len = len(word)
    count = 0

    # Helper function to check if the word exists in a direction
    def check_direction(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + i * dr, c + i * dc
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != word[i]:
                return 0
        return 1


    for r in range(rows):
        for c in range(cols):

            count += check_direction(r, c, 0, 1)  # Right
            count += check_direction(r, c, 0, -1)  # Left
            count += check_direction(r, c, 1, 0)  # Down
            count += check_direction(r, c, -1, 0)  # Up
            count += check_direction(r, c, 1, 1)  # Down-Right
            count += check_direction(r, c, 1, -1)  # Down-Left
            count += check_direction(r, c, -1, 1)  # Up-Right
            count += check_direction(r, c, -1, -1)  # Up-Left

    return count




result = count_xmas_occurrences_in_file("input.txt")
print(f"Total occurrences of XMAS: {result}")
