#!/usr/bin/python3
'''Modlue for lockboxes'''

def canUnlockAll(boxes):
    '''Unlocks all boxes with keys

    Args:
        boxes (List[List[int]]): list of lists of integers.

    Returns:
        boolean: True if all boxes can be unlocked, by using all the keys
        available in all the reachable boxes, and False otherwise.
    '''
    opened = {0}
    queue = [boxes[0]]

    while queue:
        box = queue.pop(0)
        for key in box:
            if key not in opened and key < len(boxes):
                opened.add(key)
                queue.append(boxes[key])

    return len(opened) == len(boxes)
