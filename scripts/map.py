#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Plotting the final map

fig = plt.figure()
plt.axes()
plt.xlim(-5.1, 5.1)
plt.ylim(-5.1, 5.1)
offset = 5.1
circle1 = plt.Circle((2.1 - offset, 2.1 - offset), radius=1, fill=False, ec="red")
circle2 = plt.Circle((2.1 - offset, 8.1 - offset), radius=1, fill=False, ec="red")
square1 = plt.Rectangle((0.35 - offset, 4.35 - offset), width=1.5, height=1.5, fill=False, ec="red")
square2 = plt.Rectangle((3.85 - offset, 4.35 - offset), width=2.5, height=1.5, fill=False, ec="red")
square3 = plt.Rectangle((7.35 - offset, 2.1 - offset), width=1.5, height=2, fill=False, ec="red")

plt.gca().add_patch(circle1)
plt.gca().add_patch(circle2)
plt.gca().add_patch(square1)
plt.gca().add_patch(square2)
plt.gca().add_patch(square3)
plt.axis("scaled")


plt.grid(color='lightgray',linestyle='--')

