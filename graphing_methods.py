import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd
import time
import scipy.integrate as integrate

MAX_FLOW_RATE = 25
x = []
flow_rate = []
int_flow_rate = []
sensor_on = 1

# comment out the line below if you don't want to see the plot display
# plt.ion()

figure, ax = plt.subplots(2, figsize=(7, 5))
figure.tight_layout(pad = 5.0)

line, = ax[0].plot(x, flow_rate)
ax[0].set_title("Flow rate (L/s) vs time (s)")
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Flow rate (L/m)")
ax[0].set_ylim(0, MAX_FLOW_RATE)

integral, = ax[1].plot(x, int_flow_rate)
ax[1].set_title("Volume of Water Used (L) vs time (s)")
ax[1].set_xlabel("Time (s)")
ax[1].set_ylabel("Volume (L)")

"""
    This function initializes
    all of the data arrays to
    have length of time range input t
    and initially contain only 0s
"""
def init_data(t):
    global x
    global flow_rate
    global int_flow_rate
    global figure
    global ax
    x = [i for i in range(t)]
    ax[0].set_xlim(0, t)
    ax[1].set_xlim(0, t)
    flow_rate = np.zeros(t)
    int_flow_rate = np.zeros(t)
        
"""
    This function allows you to
    change the sensor state
    between on (1) and off (0)
"""
def change_sensor_state():
    if sensor_on == 1:
        sensor_on == 0
    else:
        sensor_on == 1
"""
    This function inserts a new element y
    at the end of input list data
    and dequeues (removes) the first
    element of input list data
"""
def dequeue_insert(data, y):
    for i in range(len(data) - 1):
        data[i] = data[i + 1]
    data[len(data) - 1] = y
    
    return data

"""
    This function updates
    a single frame of the graph.

    To use it in a loop, use it like so:

    while sensor_on:
        update_graph(x_data, new_y_data)
        time.sleep(0.1)
"""
def update_graph(new_y_data):
    global flow_rate
    global int_flow_rate
    global x
    flow_rate = dequeue_insert(flow_rate, new_y_data)
    int_flow_rate = dequeue_insert(int_flow_rate, integrate.simpson(flow_rate))

    line.set_xdata(x)
    line.set_ydata(flow_rate)

    integral.set_xdata(x)
    integral.set_ydata(int_flow_rate)
    ax[1].set_ylim(0, max(int_flow_rate) + 100)

    #figure.canvas.draw()
    plt.savefig("flow.png")

    figure.canvas.flush_events()
        
    
