import numpy as np

def speedOfSound(T, h2o_x, co2_xMax):
    air_m, air_cp, air_cv = 0.02897, 1.0036, 0.7166
    h2o_m, h2o_cp, h2o_cv = 0.01801, 1.863, 1.403
    co2_m, co2_cp, co2_cv = 0.04401, 0.838, 0.649
    R = 8.31

    co2_X = []
    speed_sound = []

    for i in range (co2_xMax * 100):
        co2_x = i / 10000
        co2_X.append(co2_x * 100)

        gamma = (air_m * air_cp * (1 - h2o_x - co2_x) + h2o_m * h2o_cp * h2o_x + co2_m * co2_cp * co2_x)/(air_m * air_cv * (1 - h2o_x - co2_x) + h2o_m * h2o_cv * h2o_x + co2_m * co2_cv * co2_x)
        mu = air_m * (1 - h2o_x - co2_x) + h2o_m * h2o_x + co2_m * co2_x
        y = ((gamma * R * T) / mu) ** 0.5
        speed_sound.append(y)
    
    return co2_X, speed_sound