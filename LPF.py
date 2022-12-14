import numpy as np
import math
import random
import matplotlib.pyplot as plt

class LowPassFilter(object):
    def __init__(self, cut_off_freqency, ts):
    	# cut_off_freqency: 차단 주파수
        # ts: 주기
        
        self.ts = ts
        self.cut_off_freqency = cut_off_freqency
        self.tau = self.get_tau()

        self.prev_data = 0.
        
    def get_tau(self):
        return 1 / (2 * np.pi * self.cut_off_freqency)

    def filter(self, data):
        val = (self.ts * data + self.tau * self.prev_data) / (self.tau + self.ts)
        self.prev_data = val
        return val
    
class Sensor(object):
    def __init__(self):
        self.value = 210

    def noise(self):
        return random.uniform(-0.009, 0.009)

    def sense(self):
        self.value += self.noise()
        return math.sin(self.value) + self.noise()


if __name__ == "__main__":

    xs = []
    sensors = []
    filters = []

    lpf = LowPassFilter(60., 0.00265)
    sensor = Sensor()

    for i in range(300):
        z = sensor.sense()
        f = lpf.filter(z)

        xs.append(i)
        sensors.append(z)
        filters.append(f)

    plt.plot(xs, filters)
    plt.scatter(xs, sensors, c="r", s=1)

    plt.show()