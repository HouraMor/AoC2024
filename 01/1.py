def read_input(file_path):
    # Read the input file and parse the lists
    list1, list2 = [], []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():  # Skip empty lines
                a, b = map(int, line.split())
                list1.append(a)
                list2.append(b)
    return list1, list2

def calculate_distances(list1, list2):
    # Sort the lists in ascending order
    list1.sort()
    list2.sort()

    # Calculate distances between corresponding elements
    distances = [abs(a - b) for a, b in zip(list1, list2)]
    return distances

def main():
    file_path = "input.txt"
    list1, list2 = read_input(file_path)
    distances = calculate_distances(list1, list2)
    total_distance = sum(distances)

    print("Sorted List 1:", list1)
    print("Sorted List 2:", list2)
    print("Distances:", distances)
    print("Total Distance:", total_distance)

if __name__ == "__main__":
    main()
