#!/usr/bin/python3
"""  reads stdin line by line and computes metrics
"""
import sys

i = 0
num_files = 0
num_string = ["200", "301", "400", "401", "403", "404", "405", "500"]
callocs = [0, 0, 0, 0, 0, 0, 0, 0]

try:
    for inputs in sys.stdin:
        i += 1
        split_input = inputs.split(" ")
        if len(split_input) > 2:
            num_files += int(split_input[-1])
            status = split_input[-2]
            if status in num_string:
                j = num_string.index(status)
                callocs[j] += 1
        if (i % 10 == 0):
            print("File size: {}".format(num_files))
            for z in range(len(num_string)):
                if callocs[z] > 0:
                    print("{}: {}".format(num_string[z], callocs[z]))
except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(num_files))
    for z in range(len(num_string)):
        if callocs[z] > 0:
            print("{}: {}".format(num_string[z], callocs[z]))
