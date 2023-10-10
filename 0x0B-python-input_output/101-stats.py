#!/usr/bin/python3
""" advanced """
import sys


def print_statistics(total_size, status_codes):
    """ prints statistics """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print("{}: {}".format(status_code, status_codes[status_code]))

if __name__ == "__main__":
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 7:
                status_code = parts[-2]
                file_size = int(parts[-1])
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
