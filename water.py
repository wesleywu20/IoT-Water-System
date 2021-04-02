import matplotlib.pyplot as plt

from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates






#Graph 1: Water level vs. Day


#dates for x-axis

datesvalues = [
    datetime(2021, 3, 10),
    datetime(2021, 3, 11),
    datetime(2021, 3, 12),
    datetime(2021, 3, 13),
    datetime(2021, 3, 14),
    datetime(2021, 3, 15),
    datetime(2021, 3, 16),
    datetime(2021, 3, 17),
    datetime(2021, 3, 18),

]



Water_level=[9.5, 10.02, 7.6, 5.4, 9.8, 4.6, 8.8, 3.9, 2.8]




plt.xticks(rotation=70)
plt.plot(datesvalues,Water_level, linestyle='solid', marker='o')
plt.xlabel('day')
plt.ylabel('water level')
plt.title('Water Level vs Day')

plt.gcf().autofmt_xdate
plt.tight_layout()



plt.show()


#Graph 2: histogram of water level data
water_level2=[2,2,2, 3,4, 5,5,6,6,6,6,6]
plt.hist(water_level2, bins=7, color='purple')
plt.show()






#Graph 3: Water level vs. Hour


#hours for x-axis

datesvalues = [
    datetime(2021, 3, 10),
    datetime(2021, 3, 11),
    datetime(2021, 3, 12),
    datetime(2021, 3, 13),
    datetime(2021, 3, 14),
    datetime(2021, 3, 15),
    datetime(2021, 3, 16),
    datetime(2021, 3, 17),
    datetime(2021, 3, 18),

]



Water_level=[9.5, 10.02, 7.6, 5.4, 9.8, 4.6, 8.8, 3.9, 2.8]




plt.xticks(rotation=70)
plt.plot(datesvalues,Water_level, linestyle='solid', marker='o')
plt.xlabel('day')
plt.ylabel('water level')
plt.title('Water Level vs Day')

plt.gcf().autofmt_xdate
plt.tight_layout()



plt.show()



#Graph 3: Water level by hour
print(datetime.now());
x = [datetime.now() + datetime.timedelta(hours=i) for i in range(12)]



Water_level=[9.5, 10.02, 7.6, 5.4, 9.8, 4.6, 8.8, 3.9, 2.8]




plt.xticks(rotation=70)
plt.plot(x,Water_level, linestyle='solid', marker='o')
plt.xlabel('day')
plt.ylabel('water level')
plt.title('Water Level vs Hour')


plt.tight_layout()



plt.show()
