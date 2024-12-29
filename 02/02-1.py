def invalid_differences(report):

    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    invalid_count = sum(1 for diff in differences if not (-3 <= diff <= -1 or 1 <= diff <= 3))
    return invalid_count

def count_safe_reports(file_path):

    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                report = list(map(int, line.split()))
                invalid_count = invalid_differences(report)

                # A report is safe if it has no invalid differences or can be made safe with one removal
                if invalid_count == 0 or invalid_count == 1:
                    safe_count += 1
    return safe_count

def main():
    file_path = "input.txt"
    safe_reports = count_safe_reports(file_path)
    print(f"Number of safe reports: {safe_reports}")

if __name__ == "__main__":
    main()
