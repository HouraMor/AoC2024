def count_xmas_occurrences(file_path):
    with open(file_path, 'r') as f:

        grid = [line.strip() for line in f.readlines()]

    rows = len(grid)
    cols = len(grid[0])
    word = "MAS"
    word_len = len(word)
    count = 0


    def check_direction(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + i * dr, c + i * dc
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != word[i]:
                return 0
        return 1


    for r in range(rows):
        for c in range(cols):
            # Check in all 8 directions
            #count += check_direction(r, c, 0, 1)  # Right
            #count += check_direction(r, c, 0, -1)  # Left
            #count += check_direction(r, c, 1, 0)  # Down
            #count += check_direction(r, c, -1, 0)  # Up
            if (check_direction(r, c, 1, 1) and check_direction(r+2, c, -1, 1)): # Down-Right & Up-Right
                count +=1


            if (check_direction(r, c, -1, -1)  and check_direction(r-2, c, 1, -1)): # Up-Left&Down-Left
                count +=1
            if (check_direction(r, c, 1, 1)  and check_direction(r, c+2, 1, -1)): # Down-Right & Down-Left
                count +=1
            if (check_direction(r, c, -1, -1)  and check_direction(r, c-2, -1, 1)): # Up-Left&Up-Right
                count +=1

    return count




result = count_xmas_occurrences("input.txt")
print(f"Total occurrences of XMAS: {result}")
