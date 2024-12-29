import functools

def blink(file_path, n):
    with open(file_path, 'r') as f:
        # Read the initial stone numbers from the file and split into a list
        stones = f.read().strip().split()

    # Function to apply rules to a single stone
    @functools.cache
    def apply_rules(stone):
        new_stones = []
        if int(stone) == 0:
            # Rule 1: Stone engraved with 0 becomes 1
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            # Rule 2: Stone with even number of digits splits into two
            left_half = str(int(stone[:len(stone) // 2]))  # Remove leading zeroes
            right_half = str(int(stone[len(stone) // 2:]))
            new_stones.extend([left_half, right_half])
        else:
            # Rule 3: Stone is replaced by its value multiplied by 2024
            new_stones.append(str(2024 * int(stone)))
        return new_stones

    # Perform n blinks
    for _ in range(n):
        next_stones = []
        for stone in stones:

            next_stones.extend(apply_rules(stone))
        # Update the list of stones after this blink
        stones = next_stones


    return len(stones)


n = 75
file_path = 'input.txt'


result = blink(file_path, n)
print(f"Total number of stones: {result}")
