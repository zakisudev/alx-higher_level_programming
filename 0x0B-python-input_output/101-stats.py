#!/usr/bin/python3
"""
A module to read from stdin and computes metrics
"""


def print_stats(size, status_codes):

    """ print metrics """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == __"main"__:
    import sys

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()
            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                            status_codes[line[-2]] = 1
                        else:
                            status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)
    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
