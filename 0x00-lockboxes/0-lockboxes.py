#!/usr/bin/python3


def canUnlockAll(boxes):
    """Main funtion"""
    for key in range(1, len(boxes) - 1):

        boole = False

        for position in range(len(boxes)):

            boole = (key in boxes[position] and key != position)

            if boole is True:
                break

        if boole is False:
            return boole

    return True
