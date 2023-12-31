#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# depicting the visualization
plt.xlabel("Time (years)")
plt.ylabel("Fraction Remaining")
plt.yscale("log")
plt.plot(x, y)
plt.xlim(0, 28650)

# displaying the title
plt.title("Exponential Decay of C-14")
