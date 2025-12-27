def parse_line(line):
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return None
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }
