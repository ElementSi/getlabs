# импротирование библиотек

import numpy as np
import waveFunctions as b

def read(filename):
    with open(filename) as f:
        lines = f.readlines()

    duration = float(lines[2].split()[2])
    samples = [int(i) for i in lines[4:]]
    
    return samples, duration, len(samples)

samples_20, duration_20, length_20 = read("wave/data/20 mm.txt")
samples_40, duration_40, length_40 = read("wave/data/40 mm.txt")
samples_60, duration_60, length_60 = read("wave/data/60 mm.txt")
samples_80, duration_80, length_80 = read("wave/data/80 mm.txt")
samples_100, duration_100, length_100 = read("wave/data/100 mm.txt")
samples_120, duration_120, length_120 = read("wave/data/20 mm.txt")

x = [20]*length_20 + [40]*length_40 + [60]*length_60 + [80]*length_80 + [100]*length_100 + [120]*length_120
y = samples_20 + samples_40 + samples_60 + samples_80 + samples_100 + samples_120

print(np.polyfit(x, y, 3))