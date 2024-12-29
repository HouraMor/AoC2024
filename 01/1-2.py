from collections import Counter

def calculate_similarity_score(left_list, right_list):
    # Count occurrences of each number in the right list
    right_count = Counter(right_list)

    # Calculate similarity score
    similarity = 0
    for num in left_list:
        similarity += num * right_count.get(num, 0)

    return similarity

def read_input(file_path):
    # Read the input file and parse the lists
    left_list, right_list = [], []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():  # Skip empty lines
                a, b = map(int, line.split())
                left_list.append(a)
                right_list.append(b)
    return left_list, right_list

def main():
    file_path = "input.txt"
    left_list, right_list = read_input(file_path)
    similarity_score = calculate_similarity_score(left_list, right_list)

    print("Left List:", left_list)
    print("Right List:", right_list)
    print("Similarity Score:", similarity_score)

if __name__ == "__main__":
    main()
