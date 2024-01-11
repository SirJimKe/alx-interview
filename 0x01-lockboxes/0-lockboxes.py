#!/usr/bin/python3
"""A function to unlock boxes"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened based on available keys.
    """
    reachable_keys = set(boxes[0])
    opened_boxes = {0}

    while reachable_keys:
        new_keys = set()
        for key in reachable_keys:
            if key not in opened_boxes:
                opened_boxes.add(key)
                new_keys.update(boxes[key])

        reachable_keys = new_keys

    return len(opened_boxes) == len(boxes)
