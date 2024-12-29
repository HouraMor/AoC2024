import re

def calculate_enabled_multiplications(file_path):
    # Regular expressions for matching instructions
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    total_sum = 0
    mul_enabled = True

    with open(file_path, 'r') as file:
        for line in file:
            # Find all matches for mul, do, and don't, along with their spans
            mul_matches = [(match.span(), match.groups()) for match in re.finditer(mul_pattern, line)]
            do_matches = [match.span()[0] for match in re.finditer(do_pattern, line)]
            dont_matches = [match.span()[0] for match in re.finditer(dont_pattern, line)]

            # Iterate through each mul match and check the enabling/disabling conditions
            for i, (span, (x, y)) in enumerate(mul_matches):
                start_index = span[0]

                # Determine if mul is enabled by checking for do()/don't() between the last and current mul
                if i > 0:  # If not the first mul instruction
                    last_mul_start = mul_matches[i - 1][0][0]  # Start index of the previous mul
                    # Check if any don't() is between the last and current mul
                    if any(last_mul_start < dont < start_index for dont in dont_matches):
                        mul_enabled = False
                    # Check if any do() is between the last and current mul
                    if any(last_mul_start < do < start_index for do in do_matches):
                        mul_enabled = True


                if mul_enabled:
                    total_sum += int(x) * int(y)

    return total_sum

def main():
    file_path = "input.txt"
    result = calculate_enabled_multiplications(file_path)
    print(f"The total sum of enabled multiplications is: {result}")

if __name__ == "__main__":
    main()
