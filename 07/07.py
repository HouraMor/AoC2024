from itertools import product

def evaluate_left_to_right(numbers, operators):

    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] =='||':
            result = int(str(result) + str(numbers[i + 1]))
        elif operators[i] == '*':
            result *= numbers[i + 1]

    return result

def calculate_calibration_sum(file_path):
    total_calibration_result = 0

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue


            test_value, numbers = line.split(':')
            test_value = int(test_value)
            numbers = list(map(int, numbers.split()))

            # all possible operator combinations
            operator_combinations = product(['+','*', '||'], repeat=len(numbers) - 1)

            # if any combination produces the test value
            for operators in operator_combinations:
                if evaluate_left_to_right(numbers, operators) == test_value:
                    total_calibration_result += test_value
                    break  # No need to check further combinations for this line

    return total_calibration_result


file_path = "input.txt"
result = calculate_calibration_sum(file_path)
print(f"Total calibration result: {result}")
