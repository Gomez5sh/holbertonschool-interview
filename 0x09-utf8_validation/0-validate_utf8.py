#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Encode UTF-8
    """

    bytes_count = 0

    for num in data:
        bin_rep = format(num, '#010b')[-8:]
        if bytes_count == 0:
            for bit in bin_rep:
                if bit == '0':
                    break
                bytes_count += 1
            if bytes_count == 0:
                continue
            if bytes_count == 1 or bytes_count > 4:
                return False
        else:
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False
        bytes_count -= 1

    return bytes_count == 0
