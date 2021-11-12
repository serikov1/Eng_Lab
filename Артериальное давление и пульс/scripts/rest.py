import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.ticker as ticker
import numpy as np
from textwrap import wrap


k = 11.655455451086947 # coefficient calibrovki

with open('rest davlenie.txt', 'r') as rest:
    temprest = rest.read().split("\n")
    temprest_x = []
    temprest_y = []
    time = []
    time_time = []
    count = []
    for i in range(7, len(temprest), 1):
        temprest_y.append(int(temprest[i]) / k)
    time_time = temprest[3].split(" ")
    time = time_time[4].split(".")
    count = temprest[6].split(" ")
    temprest_x = np.linspace(0, int(time[0]), int(count[4]))


fig, ax = plt.subplots(figsize=(16, 10), dpi=200)
title = 'Артериальное давление до физической нагрузки'
ax.set_title("\n".join(wrap(title, 100)))
ax.plot(temprest_x, temprest_y, color='r', linewidth=0.3)
plt.axis([0, int(time[0]) + 5, 30, 170])
plt.ylabel('Давление [мм]', fontsize=7)
plt.xlabel('Время [с]', fontsize=7)
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax.tick_params(which='major', length=5, labelsize=5)
ax.tick_params(which='minor', length=3)
ax.grid(which='major', color='black', linewidth=0.2)
ax.minorticks_on()
ax.grid(which='minor', color='gray', linestyle=':', linewidth=0.5)
graph = mlines.Line2D([], [], color='r', markersize=30, label='Давление 140/75 мм рт.ст') 
plt.legend(handles=[graph])

plt.show()
fig.savefig("finalPressure-rest.png")