import sys
from collections import defaultdict


def parse_log_line(line: str) -> dict[str, str]:
    """Parse log file line to dictionary"""
    line_data_list = line.split(" ")
    line_data = {
        "date": line_data_list[0],
        "time": line_data_list[1],
        "level": line_data_list[2],
        "message": " ".join(line_data_list[3:])
    }
    return line_data


def load_logs(file_path: str) -> list[dict[str, str]]:
    """Load file content into list of dictionaries"""
    try:
        with open(file_path, mode="r", encoding="utf8") as f:
            return [parse_log_line(line.strip()) for line in f]

    except FileNotFoundError as e:
        print("File not found:", e)
    except UnicodeDecodeError as e:
        print("Can not decode file content:", e)
    except Exception as e:
        print("Unexpected error while opening/reading file:", e)


def filter_logs_by_level(logs: list, level: str) -> list[str]:
    """Filter logs by level, if level name is provided.
       Print filtered logs' information
    """
    for log in logs:
        if log["level"] == level:
            print(f"{log["date"]} {log["time"]} - {log["message"]}")


def count_logs_by_level(logs: list) -> dict:
    """Count logs by their level and display result to user"""
    logs_by_level = defaultdict(int)
    for log in logs:
        logs_by_level[log["level"]] += 1

    display_log_counts(logs_by_level)


def display_log_counts(counts: dict[str, int]):
    """Display a formatted table of log level counts"""
    print(f"{'Log Level':<10} | {'Quantity':<10}")
    print(f"{'-'*10} | {'-'*10}")

    for level, count in sorted(counts.items(), key=lambda i: i[1], reverse=True):
        print(f"{level:<10} | {count:<10}")
