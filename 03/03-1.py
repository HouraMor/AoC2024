import re

def calculate_sum(file_path):
    # Regular expression to match valid mul(X,Y) patterns
	#pattern = r"(mul\(\d{1,3},\d{1,3}\))" it returns mul(x,y) because The re.findall() function #in Python returns only the parts of the string that are captured by parentheses ( ) in the regular #expression.
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    total_sum = 0


    with open(file_path, 'r') as file:
        for line in file:
            # Find all valid mul(X,Y) patterns in the line
            matches = re.findall(pattern, line)

            # Calculate the sum of all valid multiplications in the line
            for x, y in matches:
                total_sum += int(x) * int(y)

    return total_sum

def main():
    file_path = "input.txt"
    result = calculate_sum(file_path)
    print(f"The total sum of all valid multiplications is: {result}")

if __name__ == "__main__":
    main()
