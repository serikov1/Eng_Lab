import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.ticker as ticker
import numpy as np


with open('40 mmHg.txt', 'r') as mm40:
    temp40 = mm40.read().split("\n")
    Sum = 0
    temp40_int = []
    for i in range(7, len(temp40) - 1, 1):
        temp40_int.append(int(temp40[i]))
    for i in range(10, len(temp40) - 1, 1):
        Sum += int(temp40[i])
    k40 = Sum / (len(temp40) - 8) / 40

    
with open('80 mmHg.txt', 'r') as mm80:
    temp80 = mm80.read().split("\n")
    Sum = 0
    for i in range(7, len(temp80) - 1, 1):
        Sum += int(temp80[i])
    k80 = Sum / (len(temp80) - 8) / 80

    
with open('120 mmHg.txt', 'r') as mm120:
    temp120 = mm120.read().split("\n")
    Sum = 0
    for i in range(7, len(temp120) - 1, 1):
        Sum += int(temp120[i])
    k120 = Sum / (len(temp120) - 8) / 120

    
with open('160 mmHg.txt', 'r') as mm160:
    temp160 = mm160.read().split("\n")
    Sum = 0
    temp160_int = []
    for i in range(7, len(temp160) - 1, 1):
        temp160_int.append(int(temp160[i]))
    for i in range(7, len(temp160) - 1, 1):
        Sum += int(temp160[i])
    k160 = Sum / (len(temp160) - 8) / 160
k = (k40 + k80 + k120 + k160) / 4


def mm_to_pas(mm):
    return mm * (13596 / 100)


pressure_calib_float = []
adc_calib_int = []
for i in range(min(temp40_int), max(temp160_int) + 1):
    adc_calib_int.append(i)
for i in range(min(temp40_int), max(temp160_int) + 1):
    pressure_calib_float.append(adc_calib_int[i - min(temp40_int)] / k)

fig, ax = plt.subplots(figsize=(16, 10), dpi=300)
plt.title('График калибровки', fontsize=7, color='black')
ax.plot(pressure_calib_float, adc_calib_int, color='r', linewidth=1)
plt.axis([35, 165, min(temp40_int) - 100, max(temp160_int) + 100])
plt.xlabel('Давление [мм]', fontsize=6)
plt.ylabel('Показания АЦП', fontsize=6)
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.yaxis.set_major_locator(ticker.MultipleLocator(200))
ax.tick_params(which='major', length=3, labelsize=3)
ax.tick_params(which='minor', length=1)
ax.grid(which='major', color='black', linewidth=0.2)
ax.minorticks_on()
ax.grid(which='minor', color='gray', linestyle=':', linewidth=0.2)
graph = mlines.Line2D([], [], color='red', markersize=30, label='Давление = Показания АЦП * k')
plt.legend(handles=[graph])

plt.show()
fig.savefig("Pressure-calibration.png")
print(k)