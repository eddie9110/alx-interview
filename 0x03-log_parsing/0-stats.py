#!/usr/bin/python3
"""
    a script that reads stdin line by line and computes metrics
"""
import sys

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                "404": 0, "405": 0, "500": 0}
file_size = 0
status_code = 0
count_ = 0


def print_result(status_codes, file_size):
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value:
            print("{}: {}".format(key, value))


try:
    for input_ in sys.stdin:
        parsed_input = input_.split()
        parsed_input = parsed_input[::-1]
        if len(parsed_input) > 2:
            count_ += 1
            if count_ <= 10:
                file_size += int(parsed_input[0])
                code = parsed_input[1]
                if (status_code in status_codes.keys()):
                    status_codes[status_code] += 1

            if (count_ == 10):
                print_result(status_codes, file_size)
                count_ = 0

finally:
    print_result(status_codes, file_size)
