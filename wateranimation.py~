
#importing libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure()
#creating a subplot
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    data = open('water.txt','r').read()
    lines = data.split('\n')
    print(lines);
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
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
