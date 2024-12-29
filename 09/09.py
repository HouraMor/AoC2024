def compact_file(file_path):

    disk_map=[]
    with open(file_path, 'r') as f:
        disk_map = f.read().strip()

    individual_blocks = []
    for i in range((len(disk_map)//2)+1):
        individual_blocks += [str(i)] * int(disk_map[2 * i])
        if 2 * i + 1 < len(disk_map):
            individual_blocks += ['.'] * int(disk_map[2 * i + 1])

    left = 0
    right = len(individual_blocks) - 1
    #print(individual_blocks)

    while left < right:
        if individual_blocks[left] == '.':
            while right > left and individual_blocks[right] == '.':
                right -= 1
            if right > left:
                individual_blocks[left], individual_blocks[right] = individual_blocks[right], '.'
        left += 1
        #right -= 1


    return individual_blocks


file_path = 'input.txt'
compact_blocks = compact_file(file_path)
#print(compact_blocks)
result = sum(i * int(e) for i, e in enumerate(filter(lambda el: el !='.', compact_blocks)))
print(f"checksum: {result}")
