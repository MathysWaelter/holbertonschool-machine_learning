#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

plt.plot(y, color="red")
plt.xlim(0.0, 10.0)
plt.ylim(0, 1000)
plt.yticks(np.arange(0, 1001, 500))

plt.show
