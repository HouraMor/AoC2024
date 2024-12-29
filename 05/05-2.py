def calculate_sum(file_path):
    with open(file_path, 'r') as f:
        data = f.read().strip().split('\n\n')

    # ordering rules
    rules = [line.strip().split('|') for line in data[0].splitlines()]
    rules = [(int(x), int(y)) for x, y in rules]


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

    # check if two pages should be swapped based on the rules
    def should_swap(x, y):
        for rule_x, rule_y in rules:
            if x == rule_x and y == rule_y:
                return False
            elif x == rule_y and y == rule_x:
                return True
        return False

    # Bubble sort function to sort the updates based on the rules
    def bubble_sort(update):
        n = len(update)
        for i in range(n):
            for j in range(0, n-i-1):
                if should_swap(update[j], update[j+1]):
                    update[j], update[j+1] = update[j+1], update[j]


    incorrect_updates = []

    # Check each update, sort them if they are incorrect, and add them to the list if they can't be sorted correctly
    total = 0
    for update in updates:



        if not is_update_correct(update):
            incorrect_updates.append(update)
        else:
            # For correct updates
            middle_page = update[len(update) // 2]
            total += middle_page

    # Sum of middle pages for incorrect updates
    incorrect_total = 0
    for update in incorrect_updates:
        sorted_update = update[:]
        bubble_sort(sorted_update)
        middle_page = sorted_update[len(update) // 2]
        incorrect_total += middle_page

    # Return the incorrect updates list and the total sums for both
    return incorrect_updates, total, incorrect_total



file_path = "input.txt"
incorrect_updates, total_sum, incorrect_sum = calculate_sum(file_path)
print(f"incorrect_updates: {incorrect_updates}")
print(f"total_sum: {total_sum}")
print(f"incorrect_sum: {incorrect_sum}")
