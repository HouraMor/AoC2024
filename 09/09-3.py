def parse_disk_map(disk_map):

    blocks = []
    for i in range(0, len(disk_map), 2):
        file_length = int(disk_map[i])
        free_space_length = int(disk_map[i + 1]) if i + 1 < len(disk_map) else 0
        if file_length > 0:
            blocks.append(('file', file_length))
        if free_space_length > 0:
            blocks.append(('free', free_space_length))
    return blocks

def expand_blocks(blocks):

    expanded = []
    file_id = 0
    for block_type, length in blocks:
        if block_type == 'file':
            expanded.extend([file_id] * length)
            file_id += 1
        else:  # 'free'
            expanded.extend(['.'] * length)
    return expanded

def compact_disk_new_method(expanded):

    n = len(expanded)

    # Find all files and their positions
    files = {}
    i = 0
    while i < n:
        if expanded[i] != '.':
            file_id = expanded[i]
            start = i
            while i < n and expanded[i] == file_id:
                i += 1
            files[file_id] = (start, i - start)  # Store file start and length
        else:
            i += 1

    # Attempt to move each file (highest ID first)
    for file_id in sorted(files.keys(), reverse=True):
        start, length = files[file_id]

        # Find the leftmost free span that can fit this file
        best_start = None
        free_length = 0
        free_start = None

        for i in range(n):
            if expanded[i] == '.':
                if free_start is None:
                    free_start = i
                free_length += 1

                if free_length >= length:
                    best_start = free_start
                    break
            else:
                free_start = None
                free_length = 0

        # If a valid span is found, move the file
        if best_start is not None and best_start < start:
            # Clear the old file position
            for i in range(start, start + length):
                expanded[i] = '.'

            # Write the file to the new position
            for i in range(best_start, best_start + length):
                expanded[i] = file_id

    return expanded

def calculate_checksum(compacted):

    checksum = 0
    for position, value in enumerate(compacted):
        if value != '.':  # Ignore free space
            checksum += position * int(value)
    return checksum

def main(file_path):

    with open(file_path, 'r') as f:
        disk_map = f.read().strip()


    blocks = parse_disk_map(disk_map)


    expanded = expand_blocks(blocks)


    compacted = compact_disk_new_method(expanded)
    print(compacted)


    checksum = calculate_checksum(compacted)

    return checksum


file_path = 'in.txt'
result = main(file_path)
print("Checksum:", result)
