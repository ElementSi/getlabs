# импротирование библиотек

import numpy as np
import matplotlib.pyplot as plt
import waveFunctions as b

def read(filename):                  # ФУКНЦИЯ ИЗ ДРУГОГО ФАЙЛА
    with open(filename) as f:
        lines = f.readlines()        # УБРАТЬ НА ПАРЕ

    duration = float(lines[2].split()[2])
    samples = np.asarray(lines[4:], dtype=int)
    
    return samples, duration, len(samples)

# чтение данных ацп для калибровки

samples_20, duration_20, length_20 = b.read("wave/data/20 mm.txt")
samples_40, duration_40, length_40 = b.read("wave/data/40 mm.txt")
samples_60, duration_60, length_60 = b.read("wave/data/60 mm.txt")
samples_80, duration_80, length_80 = b.read("wave/data/80 mm.txt")
samples_100, duration_100, length_100 = b.read("wave/data/100 mm.txt")
samples_120, duration_120, length_120 = b.read("wave/data/120 mm.txt")

# чтение данных которые должен предоставить Егор на паре

samples_wave_40, duration_wave_40, length_wave_40 = read("wave/data/wave 40 mm.txt")
samples_wave_80, duration_wave_80, length_wave_80 = read("wave/data/wave 80 mm.txt")
samples_wave_120, duration_wave_120, length_wave_120 = read("wave/data/wave 120 mm.txt")

y = [0, 20, 40, 60, 80, 100, 120]
x = [0, np.mean(samples_20), np.mean(samples_40), np.mean(samples_60), np.mean(samples_80), np.mean(samples_100), np.mean(samples_120), ]
koef = np.polyfit(x, y, 4)
poly_x = []
for i in range(2701):
    poly_x.append(i)
poly_y = []
for i in poly_x:
    poly_y.append(np.polyval(koef, i))

fig0 = plt.figure(figsize=(16, 10), dpi=400)
ax0 = plt.axes()
plt.plot(poly_y, poly_x, '#3568e7', linewidth = 3, label = 'Калибровочная функция в диапозоне  [0:2700] отсчетов АЦП')
plt.plot(y, x, 'ro', label = 'Измерения', markersize=10)
plt.xlabel('Уровень воды [мм]', fontsize = 18)
plt.ylabel('Отсчеты АЦП', fontsize = 18)
plt.title('Калибровочный график зависимости показаний АЦП от уровня', loc = 'center', fontsize = 24, wrap = True)
plt.legend(fontsize = 16)
ax0.yaxis.set_minor_locator(plt.MultipleLocator(100))
ax0.xaxis.set_minor_locator(plt.MultipleLocator(5))
ax0.grid(which = 'major', c = '#696969', linestyle = '-', linewidth = 2, alpha = 0.6)
ax0.grid(which = 'minor', c = '#696969', linestyle = '--', linewidth = 1, alpha = 0.6)
plt.xticks(np.arange(0, 150, 25), fontsize = 16)
plt.yticks(np.arange(0, 3000, 500), fontsize = 16)
plt.xlim(-15, 135)
plt.ylim(-200, 3200)
plt.savefig("wave/plots/level-calibration.png")

# ---------------------------- график для 40 мм -----------------------------------------

res_40 = np.zeros(length_wave_40)
time_res_40 = np.linspace(0, duration_wave_40, length_wave_40)

for i in range(length_wave_40):
    res_40[i] = np.polyval(koef, samples_wave_40[i])

num_devide_40 = 0

for i in range(length_wave_40):
    if res_40[i] < 37.5:
        num_devide_40 = i
        break

fig40 = plt.figure(figsize=(16, 10), dpi=400)
ax40 = plt.axes()
plt.plot(time_res_40[:num_devide_40], res_40[:num_devide_40], '#0000ff', label='Ожидание волны', linewidth = 3)
plt.plot(time_res_40[num_devide_40:], res_40[num_devide_40:], '#ff0000', label='Уровень воды в кювете', linewidth = 3)
plt.xlim(0, 15)
plt.ylim(0, 140)
plt.xticks(np.arange(0, 16, 2.5), fontsize = 16)
plt.yticks(np.arange(0, 126, 25), fontsize = 16)
ax40.yaxis.set_minor_locator(plt.MultipleLocator(5))
ax40.xaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax40.grid(which = 'major', c = '#696969', linestyle = '-', linewidth = 2, alpha = 0.6)
ax40.grid(which = 'minor', c = '#696969', linestyle = '--', linewidth = 1, alpha = 0.6)
ax40.vlines(time_res_40[num_devide_40], 0, 140, '#8473f6', linestyle = '--', linewidth = 3)
plt.title('Уровень воды в кювете после открытия торцевой двери', loc = 'center', fontsize = 24, wrap = True)
plt.xlabel('Время [с]', fontsize = 18)
plt.ylabel('Уровень воды [мм]', fontsize = 18)
plt.legend(fontsize = 20)
plt.savefig("wave/plots/velocity_40.png")

# ----------------------------- график для 80 мм -----------------------------------

res_80 = np.zeros(length_wave_80)
time_res_80 = np.linspace(0, duration_wave_80, length_wave_80)

for i in range(length_wave_80):
    res_80[i] = np.polyval(koef, samples_wave_80[i])

num_devide_80 = 0

for i in range(length_wave_80):
    if res_80[i] < 81:
        num_devide_80 = i
        break

fig80 = plt.figure(figsize=(16, 10), dpi=400)
ax80 = plt.axes()
plt.plot(time_res_80[:num_devide_80], res_80[:num_devide_80], '#0000ff', label='Ожидание волны', linewidth = 3)
plt.plot(time_res_80[num_devide_80:], res_80[num_devide_80:], '#ff0000', label='Уровень воды в кювете', linewidth = 3)
plt.xlim(0, 15)
plt.ylim(0, 140)
plt.xticks(np.arange(0, 16, 2.5), fontsize = 16)
plt.yticks(np.arange(0, 126, 25), fontsize = 16)
ax80.yaxis.set_minor_locator(plt.MultipleLocator(5))
ax80.xaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax80.grid(which = 'major', c = '#696969', linestyle = '-', linewidth = 2, alpha = 0.6)
ax80.grid(which = 'minor', c = '#696969', linestyle = '--', linewidth = 1, alpha = 0.6)
ax80.vlines(time_res_80[num_devide_80], 0, 140, '#8473f6', linestyle = '--', linewidth = 3)
plt.title('Уровень воды в кювете после открытия торцевой двери', loc = 'center', fontsize = 24, wrap = True)
plt.xlabel('Время [с]', fontsize = 18)
plt.ylabel('Уровень воды [мм]', fontsize = 18)
plt.legend(fontsize = 20)
plt.savefig("wave/plots/velocity_80.png")

# ---------------------------- график для 120 мм --------------------------

res_120 = np.zeros(length_wave_120)
time_res_120 = np.linspace(0, duration_wave_120, length_wave_120)

for i in range(length_wave_120):
    res_120[i] = np.polyval(koef, samples_wave_120[i])

num_devide_120 = 0

for i in range(length_wave_120):
    if res_120[i] < 109:
        num_devide_120 = i
        break

fig120 = plt.figure(figsize=(16, 10), dpi=400)
ax120 = plt.axes()
plt.plot(time_res_120[:num_devide_120], res_120[:num_devide_120], '#0000ff', label='Ожидание волны', linewidth = 3)
plt.plot(time_res_120[num_devide_120:], res_120[num_devide_120:], '#ff0000', label='Уровень воды в кювете', linewidth = 3)
plt.xlim(0, 15)
plt.ylim(0, 140)
plt.xticks(np.arange(0, 16, 2.5), fontsize = 16)
plt.yticks(np.arange(0, 126, 25), fontsize = 16)
ax120.yaxis.set_minor_locator(plt.MultipleLocator(5))
ax120.xaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax120.grid(which = 'major', c = '#696969', linestyle = '-', linewidth = 2, alpha = 0.6)
ax120.grid(which = 'minor', c = '#696969', linestyle = '--', linewidth = 1, alpha = 0.6)
ax120.vlines(time_res_120[num_devide_120], 0, 140, '#8473f6', linestyle = '--', linewidth = 3)
plt.title('Уровень воды в кювете после открытия торцевой двери', loc = 'center', fontsize = 24, wrap = True)
plt.xlabel('Время [с]', fontsize = 18)
plt.ylabel('Уровень воды [мм]', fontsize = 18)
plt.legend(fontsize = 20)