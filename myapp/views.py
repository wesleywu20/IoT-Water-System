from django.shortcuts import render
from django.template import RequestContext


from django.shortcuts import render




    #importing libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib

import plotly
import plotly.graph_objects as go


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

    config={'responsive':True}
    graph1=plotly.offline.plot(fig1, auto_open=False, output_type="div", config=config)
    return render(request, 'index.html', {'active_page': 'index.html', 'graph1':graph1})



# --> your matplotlib commands <--



# Create your views here.
