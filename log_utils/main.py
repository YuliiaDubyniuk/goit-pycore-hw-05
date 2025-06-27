import sys
import log_parser

log_levels = ("INFO", "DEBUG", "ERROR", "WARNING")


def main():
    """
       Parse CLI command to get log file path, open and read file.
       Display summary table and filter by log level, if user provides level name.
    """
    if len(sys.argv) >= 2:
        f_path = sys.argv[1]
        logs = log_parser.load_logs(f_path)
        if logs:
            log_parser.count_logs_by_level(logs)
            if len(sys.argv) > 2:
                level = sys.argv[2].upper()
                if level in log_levels:
                    log_parser.filter_logs_by_level(logs, level)
                else:
                    print(
                        f"Invalid log level. Please enter one of the following {str(log_levels)}.")
    else:
        print("File path has not been provided.")


if __name__ == "__main__":
    main()
