import time
import numpy as np
import waveFunctions as b

try:
    b.initSpiAdc()
    
    print("Are you taking dynamic or static measurments?\nPress D for dynamic or S for static")
    type = input()
    print("What is the deapth of the water?")
    deapth = input()

    if type == 'D':
        duration = 15
        b.waitForOpen()
    else:
        duration = 10

    data = np.empty(0)
    counter = 0
    start = time.time()
    finish = start

    while (finish - start) < duration:
        counter = counter + 1
        data = np.append(data, b.getAdc())
        finish = time.time()

    if type == 'D':
        b.save_dynamic(deapth, data, start, finish)
    else:
        b.save_static(deapth, data, start, finish)

finally:
    b.deinitSpiAdc()