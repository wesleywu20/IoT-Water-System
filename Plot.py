
<<<<<<< HEAD
import numpy as np
=======
import numpy as numpy
>>>>>>> a1e1b59fdcf11e0263e50424555168c866ed151e
import pandas
import matplotlib
import matplotlib.pyplot as plt

testData = np.array([1,3,54,2,4,6,234,1,6,2,3,2,64])
time = np.linspace(0, 10, num = len(testData))

plt.plot(time, testData)

plt.xlabel("Time")
plt.ylabel("Flow Rate")
<<<<<<< HEAD
plt.show()
=======
plt.show()
>>>>>>> a1e1b59fdcf11e0263e50424555168c866ed151e
