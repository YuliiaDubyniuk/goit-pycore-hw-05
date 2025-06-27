import sys
import log_parser

log_levels = ("INFO", "DEBUG", "ERROR", "WARNING")


def main():
    if len(sys.argv) >= 2:
        f_path = sys.argv[1]

        if len(sys.argv) > 2 and sys.argv[2].upper() in log_levels:
            log_parser.filter_logs_by_level(logs, level)
        else:
            print(
                f"Invalid log level. Please enter one of the following {str(log_levels)}.")
    else:
        print("File path has not been provided")
    return f_path, log_level


if __name__ == "__main__":
    main()
