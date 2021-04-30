import dataAnalysis as dA

# Iterative Values:
flowData = [1,2,3,4,5,6,7,8,9,0,2,14,6,7,3,2,4,7,3,4,4,3,14,13,23,12,10]
numValues = len(flowData)
prevFlowMean = 0
callNum = 0
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

flowMean = dA.meanFlowRate(prevFlowMean, flowData, numValues, callNum)
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