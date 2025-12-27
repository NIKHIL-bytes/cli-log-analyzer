import sys
from utils import parse_line
from colorama import Fore, Style

def analyze(file_path):
    stats = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    try:
        with open(file_path, "r") as f:
            for line in f:
                data = parse_line(line)
                if not data:
                    continue

                level = data["level"]
                if level in stats:
                    stats[level] += 1

                if level == "ERROR":
                    print(Fore.RED + line.strip())
                elif level == "WARNING":
                    print(Fore.YELLOW + line.strip())
                else:
                    print(Fore.GREEN + line.strip())

    except FileNotFoundError:
        print("File not found")

    print(Style.RESET_ALL)
    print("Summary:")
    for k, v in stats.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyzer.py <logfile>")
    else:
        analyze(sys.argv[1])
