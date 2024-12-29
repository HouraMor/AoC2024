def compact_file_v2_optimized(file_path):

    with open(file_path, 'r') as f:
        disk_map = f.read().strip()


    individual_blocks = []
    file_size = []
    free_space = []

    #file_id = 0
    for i in range(len(disk_map) // 2):
        file_size.append(int(disk_map[2 * i]))
        free_space.append(int(disk_map[2 * i + 1]))

        #file_id += 1

    file_ids = [i for i in range(len(file_size))]

    # Process files in decreasing file ID order
    max_file_id = len(file_size)
    #n = len(individual_blocks)
    free_start = 0  # Pointer to the start of the current free space span

    for file_id in range(max_file_id, -1, -1):
        # Find the file's blocks
        for i in range(len(free_space))
        file_positions = [i for i, block in enumerate(individual_blocks) if block == str(file_id)]
        if not file_positions:
            continue

        file_size = len(file_positions)

        # Move free_start to the beginning of the next free span
        while free_start < n and individual_blocks[free_start] != '.':
            free_start += 1

        # Look for a span of free space that can fit the file, to the left of the file
        target_start = None
        temp_start = free_start
        free_count = 0
        for i in range(free_start, file_positions[0]):
            if individual_blocks[i] == '.':
                free_count += 1
                if free_count == file_size:
                    target_start = i - file_size + 1
                    break
            else:
                free_count = 0

        if target_start is not None:
            # Move the file
            for pos in file_positions:
                individual_blocks[pos] = '.'
            for i in range(file_size):
                individual_blocks[target_start + i] = str(file_id)

            # Update free_start to skip over the newly filled span
            free_start = target_start + file_size

    # Calculate the checksum
    checksum = sum(i * int(block) for i, block in enumerate(individual_blocks) if block != '.')
    return checksum



file_path = 'input.txt'
result = compact_file_v2_optimized(file_path)
print(f"Checksum: {result}")
