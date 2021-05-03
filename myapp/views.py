from django.shortcuts import render
from django.template import RequestContext


from django.shortcuts import render

import numpy as np
import scipy as sp
import pandas as pd
import time
import scipy.integrate as integrate

from myapp import sql_helpers as db
from myapp import dataAnalysis as da
import sqlite3
from sqlite3 import Error


import datetime as dt


#importing libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib

import plotly
import plotly.graph_objects as go

from myapp import dataanalysis
flowData=[5,6,10,8,9,2,3]
flowMean=dataanalysis.meanFlowRate(2.5,flowData,7)
flowMean=str.format("{:.2f}".format(flowMean))
totalWaterUsed=dataanalysis.totalWaterUsed(5, flowData, 5)
totalWaterUsed=str.format("{:.2f}".format(totalWaterUsed))
maxFlow=dataanalysis.maxFlow(10, flowData)
maxFlow=str.format("{:.2f}".format(maxFlow))




# ----------------- graphing_methods.py ---------------------------------

# Graph labels
MAX_FLOW_RATE = 25
x = []
flow_rate = []
int_flow_rate = []

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

def index(request):

    global flow_rate
    global int_flow_rate
    global x
    
    flow_rate.clear()
    int_flow_rate.clear()
    
    now = dt.datetime.now()
    times, flow_rate = db.get_range((now - dt.timedelta(seconds = 100000000)).strftime('%Y-%m-%d %H:%M:%S.%f'), now)
    temp = []
    for flow in flow_rate:
        temp.append(flow)
        int_flow_rate.append(integrate.simps(temp))

    line.set_xdata(times)
    line.set_ydata(flow_rate)

    integral.set_xdata(x)
    integral.set_ydata(int_flow_rate)
    ax[1].set_ylim(0, max(int_flow_rate) + 100)
    
    fig2 = go.Figure()
    fig2.add_scatter(x=times, y=int_flow_rate, mode='lines', name='current values')
    
    fig2.update_layout(
        title_text="Total Water Flow vs Time",
    )

    # -------------------------------------

    xs = times
    ys = flow_rate

    fig = plt.figure()
    #creating a subplot
    ax1 = fig.add_subplot(1,1,1)

    ax1.clear()
    ax1.plot(xs, ys)

    plt.xlabel('Date')
    plt.ylabel('Water temperature')
    plt.title('Water temperature vs. Date')

    plt.autoscale()




    fig1=go.Figure()
    fig1.add_scatter(x=xs, y=ys, mode='lines', name='current values')

    fig1.update_layout(
        title_text="Water Flow vs Time",
        width=550,
        height=500,
    )


    
    fig2.update_layout(
    #    title_text="Graph of Water Levels",
        width=900,
        height=700,
    )

    config={'responsive':True}

    # weather="sunny"

    graph1=plotly.offline.plot(fig1, auto_open=False, output_type="div", config=config)
    graph2= plotly.offline.plot(fig2, auto_open=False, output_type="div", config=config)
    return render(request, 'index.html', {'active_page': 'index.html', 'graph1':graph1, 'graph2':graph2, "flowMean":flowMean, "totalWaterUsed":totalWaterUsed, "maxFlow":maxFlow})




# --> your matplotlib commands <--



# Create your views here.
