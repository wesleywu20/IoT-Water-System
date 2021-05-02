''' This program demonstrates some of the data analysis functions from the data analysis program,
    dataAnalysis.py. The functions are demonstrated in the order that they are included in the program.
    Both session-scope and lifetime-scope functions are included. For both sets of functions, the iterative
    values that the program uses would be changed and fed back into the functions and loops with each iteration
    of the main program, synchronously with the updating cycles of the graph. As such, this program just shows
    a single slice in time of a much larger process. '''

''' Some aspects of the program could be implemented in a more streamlined manner, like the variables being set
    after the print statements that could be set beforehand just as easily. However, this is kept for easy comprehensibility. '''

import datetime as dt
import numpy as np
import dataAnalysis as dA

# Iterative Values:
flowData = [1,2,3,4,5,6,7,8,9,0,2,14,6,7,3,2,4,7,3,4,4,3,14,13,23,12,10]    # Actual flow data is taken from the database
numValues = len(flowData)                                                   # Taken either From length of flowData or specified number of values in window
flowMean = 0                                                            # Taken from current value of prevFlowMean from iterative caller function
freq = 30000                                                                # Specified fixed frequency of data samples per minute
waterUsed = 1                                                           # Taken from current value of prevWaterUsed from iterative caller function
flowMax = 18.67                                                         # Taken from current value of prevMaxFlow from iterative caller function

# MetaData Values:
flowTimes = ["2021-04-16 15:41:44.952130", "2021-04-16 15:41:45.266081", "2021-04-16 15:41:45.610755", "2021-04-16 15:41:45.957314",
             "2021-04-16 15:41:46.302279", "2021-04-16 15:41:46.650486", "2021-04-16 15:41:46.692330", "2021-04-16 15:41:46.719504", 
             "2021-04-16 15:41:46.745066", "2021-04-16 15:41:46.769784", "2021-04-16 15:41:46.795690", "2021-04-16 15:41:46.826209", 
             "2021-04-16 15:41:46.859528", "2021-04-16 15:41:46.890260", "2021-04-16 15:41:46.915434", "2021-04-16 15:41:46.938503"]
for i in range(len(flowTimes)):
    flowTimes[i] = dt.datetime.strptime(flowTimes[i], '%Y-%m-%d %H:%M:%S.%f')
histogram = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
netWaterUsed = 3
meanWaterUsed = 2
totalNumValues = 100

# ============ Testing of session-scope functions: ============

print("")

flowMean = dA.meanFlowRate(flowMean, flowData, numValues)
print("Your mean flow rate is", flowMean, "Liters per minute")

waterUsed = dA.totalWaterUsed(waterUsed, flowData, freq)
print("You have used", waterUsed, "Liters of water")

flowMax = dA.maxFlow(flowMax, flowData)
print("The maximum flow rate you reached is", flowMax, "Liters per minute")

waterRunning = dA.state(flowData[len(flowData) - 1])
if waterRunning:
    print("The water is running!")
else:
    print("The water is not running")

# ============ Testing of lifetime-scope functions: ============

histogram = dA.usageTimes(histogram, flowTimes)
modeTime = np.where(histogram == np.amax(histogram))
modeTime = modeTime[0]
modeTime = modeTime[0]
if modeTime > 12:
    modeTime = modeTime - 12
    dayNight = "PM"
else:
    dayNight = "AM"
print("You used water most commonly between", modeTime, "and", modeTime + 1, dayNight)

netWaterUsed = dA.totalWater(netWaterUsed, waterUsed)
print("Since installing this system, you have used", netWaterUsed, "Liters of water")

meanWaterUsed = dA.meanWater(flowMean, numValues, meanWaterUsed, totalNumValues)
print("The average water flow rate for all time is", meanWaterUsed, "Liters per minute")

print("")