
import numpy as np
import pandas 
import matplotlib
import matplotlib.pyplot as plt
import scipy

testData = np.array([1,2,3,4,5,6,7,8,9,10,11])
yvals = np.array([1,3,54,1,2,7,4,123,4,45,6])

plt.plot (testData, yvals )
 
plt.xlabel("Time")
plt.ylabel("Flow Rate")
#plt.xlim(0,50)
#plt.ylim(0,70)
plt.show()