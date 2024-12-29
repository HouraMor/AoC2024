from collections import Counter

def blink_optimized(file_path, n):
    with open(file_path, 'r') as f:
        # Read the initial stone numbers from the file
        initial_stones = list(map(int, f.read().strip().split()))

    # Group stones by their values using a Counter using BATCH PROCESSING
    stones = Counter(initial_stones)

    for _ in range(n):
        next_stones = Counter()
        for stone, count in stones.items():
            if stone == 0:
                # 0 becomes 1
                next_stones[1] += count
            elif len(str(stone)) % 2 == 0:
                # Even-length stones split into two
                half_len = len(str(stone)) // 2
                left = int(str(stone)[:half_len])
                right = int(str(stone)[half_len:])
                next_stones[left] += count
                next_stones[right] += count
            else:
                # Odd-length stones multiply by 2024
                next_stones[stone * 2024] += count

        stones = next_stones


    return sum(stones.values())


n = 75
file_path = 'input.txt'


result = blink_optimized(file_path, n)
print(f"Total number of stones: {result}")
