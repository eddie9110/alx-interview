#!/usr/bin/python3
"""Module for canUnlockAll function"""


def canUnlockAll(boxes):
    """Function determines if all boxes can be opened"""
    opened_boxes = [0] # box 0 is already unlocked
    for box in opened_boxes:
        for key in boxes[box]:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.append(key)

    return len(opened_boxes) == len(boxes)
