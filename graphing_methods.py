import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd
import time

MAX_FLOW_RATE = 25
x = []
flow_rate = []
    
plt.title("Flow rate (L/min) vs time (s)")
plt.xlabel("Time (s)")
plt.ylabel("Flow rate (L/min)")
plt.ylim(0, MAX_FLOW_RATE)

plt.ion()

figure, ax = plt.subplots(figsize=(7, 5))
line, = ax.plot(x, flow_rate)

def init_data(t):
    x = [i for i in range(t)]
    plt.xlim(0, t)
    flow_rate = np.zeros(t)

def dequeue_insert(data, y):
    for i in range(len(data) - 1):
        data[i] = data[i + 1]
    data[len(data) - 1] = y
    
    return data

def update_graph(sensor_on, x_data, new_y_data):
    while sensor_on:
        flow_rate = dequeue_insert(flow_rate, new_y_data)

        line.set_xdata(x_data)
        line.set_ydata(flow_rate)

        figure.canvas.draw()

        figure.canvas.flush_events()
        time.sleep(0.1)
