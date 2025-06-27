import sys
from collections import defaultdict


def get_log_file_path() -> str:
    f_path = ""
    if len(sys.argv) >= 2:
        f_path = sys.argv[1]
        log_level = sys.argv[2] if len(sys.argv) > 2 else None
    else:
        print("File path has not been provided")
    return f_path, log_level


log_file_path, log_level = get_log_file_path()


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
    try:
        with open(file_path, encoding="utf8") as f:
            return [parse_log_line(line.strip()) for line in f]

    except FileNotFoundError as e:
        print("File not found:", e)
        return []
    except UnicodeDecodeError as e:
        print("Can not decode file content:", e)
        return []
    except Exception as e:
        print("Unexpected error while opening/reading file:", e)
        return []


def filter_logs_by_level(logs: list, level: str) -> list[str]:
    """Filter logs by level if provided"""
    for log in logs:
        if log["level"].upper() == level:
            print(f"{log["date"]} {log["time"]} - {log["message"]}")


def count_logs_by_level(logs: list) -> dict:
    logs_by_level = defaultdict(int)
    for log in logs:
        logs_by_level[log["level"]] += 1

    display_log_counts(logs_by_level)


def display_log_counts(counts: dict[str, int]):
    print(f"{'Log Level':<20} | {'Quantity':<10}")
    print(f"{'-'*20} | {'-'*10}")

    for level, count in sorted(counts.items()):
        print(f"{level:<20} | {count:<10}")
