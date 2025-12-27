# cli-log-analyzer

## About

CLI Log Analyzer is a small Python project created to practice working with command line tools and log files.  
It reads a log file, highlights different log levels using colors, and shows a basic summary.

The goal of the project was to improve understanding of file handling, modular code, and CLI-based programs.

## Rules

- Log file must be a plain text file
- Each log entry should be on a new line
- Supported log levels are INFO, WARNING, and ERROR
- Log format must follow the pattern:
  YYYY-MM-DD HH:MM:SS LEVEL Message
- Empty or invalid lines are ignored
- The tool does not modify or store any log data

## Usage

Run the analyzer by passing the log file as an argument:

python analyzer.py <logfile>

Example:
python analyzer.py sample.log

## Output

- INFO messages are shown in green
- WARNING messages are shown in yellow
- ERROR messages are shown in red
- A summary count is displayed at the end
