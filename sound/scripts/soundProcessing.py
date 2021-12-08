import numpy as np
import matplotlib.pyplot as plt
import soundFunctions as b

air_m, air_cp, air_cv = 0.02897, 1.0036, 0.7166
h2o_m, h2o_cp, h2o_cv = 0.01801, 1.863, 1.403
co2_m, co2_cp, co2_cv = 0.04401, 0.838, 0.649
R = 8.31
dalton = 1.661 * (10 ** -27)
p0 = 100000
length = 1.158

print("Enter the limit of co2 concentration on graph [%]")
co2_xMax = int(input())

print("Enter the time of sound propagation in atmospheric air [ms]")
time_1 = float(input())
time_1 = time_1 / 1000
speed_1 = length / time_1

print("Enter the time of sound propagation in air saturated with co2 [ms]")
time_2 = float(input())
time_2 = time_2 / 1000
speed_2 = length / time_2

with open("sound/data/conditions.txt") as f:
    lines = f.readlines()

abs_humidity = float(lines[0].split()[3])
t = float(lines[1].split()[2])

T = t + 273.16

h20_n = abs_humidity / (h2o_m * 1000 * dalton)
air_n = p0 / (1000 * dalton * R * T)

h2o_x = h20_n / air_n

co2_X, speed_sound = b.speedOfSound(T, h2o_x, co2_xMax)

koef = np.polyfit(speed_sound, co2_X, 1)

co2_x_1 = np.polyval(koef, speed_1)
co2_x_2 = np.polyval(koef, speed_2)

fig = plt.figure(figsize=(16, 10), dpi=400)
ax = plt.axes()
plt.plot(co2_X, speed_sound, '#0000ff', label='Аналитическая зависимость', linewidth = 3)
plt.plot(co2_x_1, speed_1, marker = 'p', c = '#ed6341', label = 'Значение в воздухе', markersize = 15, linewidth = 0)
plt.plot(co2_x_2, speed_2, marker = 'p', c = '#32e741', label = 'Значение в выдохе', markersize = 15, linewidth = 0)
plt.xlim(0, co2_xMax)
plt.ylim(338, 348)
plt.xticks(np.arange(0, co2_xMax + 1, 1), fontsize = 16)
plt.yticks(np.arange(338, 348, 2), fontsize = 16)
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.4))
ax.grid(which = 'major', c = '#696969', linestyle = '-', linewidth = 2, alpha = 0.6)
ax.grid(which = 'minor', c = '#696969', linestyle = '--', linewidth = 1, alpha = 0.6)
plt.title('Зависимость скорости звука от коннцентрации co2', loc = 'center', fontsize = 24, wrap = True)
plt.xlabel('Концентрация co2 [%]', fontsize = 18)
plt.ylabel('Скорость звука [м/c]', fontsize = 18)
plt.legend(fontsize = 20)
plt.savefig("sound/plots/speed-of-sound.png")