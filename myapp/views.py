from django.shortcuts import render
from django.template import RequestContext


from django.shortcuts import render





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



def index(request):







    fig = plt.figure()
    #creating a subplot
    ax1 = fig.add_subplot(1,1,1)


    data = open('myapp/water.txt','r').read()
    lines = data.split('\n')
    #print(lines);
    xs = []
    ys = []


    for line in lines:
        if line:
            word=line.split(",")
            if (len(word)>1):
                ys.append((float(word[1])))
                xs.append((word[0]))



    ax1.clear()
    ax1.plot(xs, ys)

    plt.xlabel('Date')
    plt.ylabel('Water temperature')
    plt.title('Water temperature vs. Date')

    plt.autoscale()




    fig1=go.Figure()
    fig1.add_scatter(x=xs, y=ys, mode='lines', name='current values')

    fig1.update_layout(
    #    title_text="Graph of Water Levels",
        width=550,
        height=500,
    )


    fig2=go.Figure()
    fig2.add_scatter(x=xs, y=ys, mode='lines', name='current values')

    fig2.update_layout(
    #    title_text="Graph of Water Levels",
        width=900,
        height=700,
    )

    config={'responsive':True}
    # weather="sunny"

    graph1=plotly.offline.plot(fig1, auto_open=False, output_type="div", config=config)
    graph2= plotly.offline.plot(fig1, auto_open=False, output_type="div", config=config)
    return render(request, 'index.html', {'active_page': 'index.html', 'graph1':graph1, 'graph2':graph2, "flowMean":flowMean, "totalWaterUsed":totalWaterUsed, "maxFlow":maxFlow})






# --> your matplotlib commands <--



# Create your views here.
