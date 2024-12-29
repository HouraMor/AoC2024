def is_safe(report):

    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are between -3 and -1 (decreasing) or 1 and 3 (increasing)
    if all(-3 <= diff <= -1 for diff in differences) or all(1 <= diff <= 3 for diff in differences):
        return True
    return False

def safe_with_one_removal(report):

    for i in range(len(report)):
        # Create a new report by removing the level at index i
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

def count_safe_reports(file_path):

    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                report = list(map(int, line.split()))
                if is_safe(report) or safe_with_one_removal(report):
                    safe_count += 1
    return safe_count

def main():
    file_path = "input.txt"
    safe_reports = count_safe_reports(file_path)
    print(f"Number of safe reports: {safe_reports}")

if __name__ == "__main__":
    main()
