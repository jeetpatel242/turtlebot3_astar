#!/usr/bin/env python3

import numpy as np
import math


# Function to check if the given point lies outside the final map or in the obstacle space
def check_node(node, clearance):
    # Checking if point inside map
    offset = 5.1
    if node[0] + clearance >= 10.1 - offset or node[0] - clearance <= 0.1 - offset or node[1] + clearance >= 10.1 - offset or node[1] - clearance <= 0.1 - offset:
        print('Sorry the point is out of bounds! Try again.')
        return False
    # Checking if point inside circles
    elif ((node[0] - (2.1 - offset)) ** 2 + (node[1] - (2.1 - offset)) ** 2 - (1 + clearance) ** 2 < 0):  # circle
        print('Sorry the point is in the circle 1 obstacle space! Try again')
        return False
    elif ((node[0] - (2.1 - offset)) ** 2 + (node[1] - (8.1 - offset)) ** 2 - (1 + clearance) ** 2 < 0):  # circle
        print('Sorry the point is in the circle 2 obstacle space! Try again')
        return False

    # Checking if point inside squares
    elif (((node[0] - (0.35 - offset) + clearance > 0) and (node[0] - (1.85 - offset) - clearance < 0)) and (
            (node[1] - (4.35 - offset) + clearance > 0) and (node[1] - (5.85 - offset) - clearance < 0))):
        print('Sorry the point is in the square 1 obstacle space! Try again')
        return False
    elif (((node[0] - (3.75 - offset) + clearance > 0) and (node[0] - (6.45 - offset) - clearance < 0)) and (
            (node[1] - (4.25 - offset) + clearance > 0) and (node[1] - (5.95 - offset) - clearance < 0))):
        print('Sorry the point is in the square 2 obstacle space! Try again')
        return False
    elif (((node[0] - (7.35 - offset) + clearance > 0) and (node[0] - (8.85 - offset) - clearance < 0)) and (
            (node[1] - (2.10 - offset) + clearance > 0) and (node[1] - (4.10 - offset) - clearance < 0))):
        print('Sorry the point is in the square 3 obstacle space! Try again')
        return False
    else:
        return True
