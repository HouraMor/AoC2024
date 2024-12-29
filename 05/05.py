def calculate_sum(file_path):
    with open(file_path, 'r') as f:
        data = f.read().strip().split('\n\n')

    # ordering rules
    rules = [line.strip().split('|') for line in data[0].splitlines()]
    rules = [(int(x), int(y)) for x, y in rules]

    # Parse updates
    updates = [list(map(int, update.split(','))) for update in data[1].splitlines()]

    # check if an update respects the rules
    def is_update_correct(update):
        update_set = set(update)
        positions = {page: idx for idx, page in enumerate(update)}
        for x, y in rules:
            if x in update_set and y in update_set:
                if positions[x] > positions[y]:
                    return False
        return True


    total = 0
    for update in updates:
        if is_update_correct(update):
            # middle page
            middle_page = update[len(update) // 2]
            total += middle_page

    return total




result = calculate_sum("input.txt")
print(f"Sum: {result}")
