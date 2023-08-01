#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

person = ['Farrah', 'Fred', 'Felicia']
fruits = ['Apples', 'Bananas', 'Oranges', 'Peaches']

colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

fig, ax = plt.subplots()

bar_positions = np.arange(len(person))

bottom = np.zeros(len(person))
for i, fruits in enumerate(fruits):
    ax.bar(bar_positions, fruit[i, :], width=0.5,
           bottom=bottom, label=fruits, color=colors[i])
    bottom += fruit[i, :]

ax.set_ylabel('Quantity of Fruit')
ax.set_title('Number of Fruit per Person')
ax.set_ylim(0, 80)
ax.set_yticks(np.arange(0, 81, 10))
ax.set_xticks(bar_positions)
ax.set_xticklabels(person)
ax.legend()

plt.show()
