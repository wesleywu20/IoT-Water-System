''' This program demonstrates some of the data analysis functions from the data analysis program,
    dataAnalysis.py. The functions are demonstrated in the order that they are included in the program.
    Both session-scope and lifetime-scope functions are included. For both sets of functions, the iterative
    values that the program uses would be changed and fed back into the functions and loops with each iteration
    of the main program, synchronously with the updating cycles of the graph. As such, this program just shows
    a single slice in time of a much larger process. '''

''' Some aspects of the program could be implemented in a more streamlined manner, like the variables being set
    after the print statements that could be set beforehand just as easily. However, this is kept for easy comprehensibility. '''

import dataAnalysis as dA

# Iterative Values:
flowData = [1,2,3,4,5,6,7,8,9,0,2,14,6,7,3,2,4,7,3,4,4,3,14,13,23,12,10]
numValues = len(flowData)
prevFlowMean = 0
freq = 30000
prevWaterUsed = 1
prevMaxFlow = 18.67

# MetaData Values:
# flowTimes = time data from database
histogram = 0 * [24]
netWaterUsed = 3
meanWaterUsed = 2
totalNumValues = 100

# ============ Testing of session-scope functions: ============

flowMean = dA.meanFlowRate(prevFlowMean, flowData, numValues)
print("Your mean flow rate is", flowMean, "Liters per minute")
prevFlowMean = flowMean

waterUsed = dA.totalWaterUsed(prevWaterUsed, flowData, freq)
print("You have used", waterUsed, "Liters of water")
prevWaterUsed = waterUsed

flowMax = dA.maxFlow(prevMaxFlow, flowData)
print("The maximum flow rate you reached is", flowMax, "Liters per minute")
prevMaxFlow = flowMax

waterRunning = dA.state(flowData[len(flowData) - 1])
if waterRunning:
    print("The water is running!")
else:
    print("The water is not running")

# ============ Testing of lifetime-scope functions: ============

# testing for usageTimes needs time data

netWaterUsed = dA.totalWater(netWaterUsed, waterUsed)
print("Since installing this system, you have used", netWaterUsed, "Liters of water")

meanWaterUsed = dA.meanWater(flowMean, numValues, meanWaterUsed, totalNumValues)
print("The average water flow rate for all time is", meanWaterUsed, "Liters per minute")