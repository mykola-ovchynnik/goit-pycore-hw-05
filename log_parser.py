import sys
from collections import Counter


def parse_log_line(line):
    parts = line.split(" ", 3)
    return {"date": parts[0], "time": parts[1], "level": parts[2], "message": parts[3]}


def load_logs(file_path):
    try:
        with open(file_path, "r") as file:
            for line in file:
                yield parse_log_line(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)


def filter_logs_by_level(logs, level):
    return [log for log in logs if log["level"] == level.upper()]


def count_logs_by_level(logs):
    levels = [log["level"] for log in logs]
    return Counter(levels)


def display_log_counts(counts):
    print("Log level  | Amount")
    print("-----------|----------")
    for level, count in counts.items():
        print(f"{level:<10} | {count}")


def display_filtered_logs(logs, level, counts):
    level = level.upper()
    if level not in counts:
        print(f"Error: Log level '{level}' not found in the logs.")
        sys.exit(1)
    filtered_logs = filter_logs_by_level(logs, level)
    print(f"\nLog details for level '{level}':")
    for log in filtered_logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python log_parser.py <path_to_logfile> [log_level]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = list(load_logs(file_path))
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) == 3:
        display_filtered_logs(logs, sys.argv[2], counts)


if __name__ == "__main__":
    main()
