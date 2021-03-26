
import numpy as np
import numpy as numpy
import pandas
import matplotlib
import matplotlib.pyplot as plt

testData = np.array([1,3,54,2,4,6,234,1,6,2,3,2,64])
time = np.linspace(0, 10, num = len(testData))

plt.plot(time, testData)

plt.xlabel("Time")
plt.ylabel("Flow Rate")
plt.show()