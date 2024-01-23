#!/usr/bin/python3
"""Log parsing"""
import sys
import signal

# Define the status codes
STATUS_CODES = {200, 301, 400, 401, 403, 404, 405, 500}

# Initialize variables
total_size = 0
lines_count = 0
status_counts = {str(code): 0 for code in sorted(STATUS_CODES)}

def print_statistics():
    print(f"Total file size: {total_size}")
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{code}: {count}")
    print()

def signal_handler(signal, frame):
    print("\nStatistics before interruption:")
    print_statistics()
    sys.exit(0)

# Set up signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        # Split the line and check if it matches the specified format
        parts = line.split()
        if len(parts) >= 10 and parts[5] == '"GET' and parts[7].isdigit() and parts[8].isdigit():
            status_code = parts[8]
            file_size = int(parts[9])

            # Update metrics
            total_size += file_size
            status_counts[status_code] += 1
            lines_count += 1

            # Print statistics every 10 lines
            if lines_count % 10 == 0:
                print_statistics()

except KeyboardInterrupt:
    print("\nStatistics before interruption:")
    print_statistics()
    sys.exit(0)
