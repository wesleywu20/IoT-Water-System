import numpy as np
import sql_helpers as db
from datetime import datetime, timedelta

''' For each new graph frame generated, calculate the following data '''

''' Variables passed into functions from caller: '''
# flowData = flow data points from database since start of desired window
# numValues = number of values since the start of desired window - i.e. number of elements in flowData array: numValues = len(flowData)
# callNum = the current iteration index of the caller program (frame number of graph) - starts at 1, maintained by caller - needs fixed window size

# freq = approximate frequency per minute of data sampling - can be approximated, but should be rather high - used for integration

# prevFlowMean = previous flow mean value for session still stored in looping caller function
# prevWaterUsed = prevous water used value for session still stored in looping caller function
# prevMaxFlow = previous max flow value for session still stored in looping caller function
# finalDataPoint = final point in flow data array, flowData[len(flowData) - 1]

# timesUsed = time array with all times water is used from db
# netWaterUsed = total amount of water used from db metadata
# meanWaterUsed = mean of all values in db from db metadata
# totalNumValues = total number of values in db from db metadata

# flowTimes = times water is used from current session/frame/window from database

callNum = 0

# Running average flow rate for current user session
def meanFlowRate(prevFlowMean, flowData, numValues):
    global callNum
    totalNum = callNum * numValues + numValues
    wavg1 = np.mean(flowData) * numValues
    wavg2 = prevFlowMean * numValues * callNum
    flowMean = (wavg1 + wavg2)/totalNum
    callNum += 1
    return flowMean

# Total water used throughout session - integral of flow rate over time
def totalWaterUsed(prevWaterUsed, flowData, freq):
    waterUsed = (np.trapz(flowData)/freq + prevWaterUsed)
    return waterUsed

# Maximum flow rate attained throughout session
def maxFlow(prevMaxFlow, flowData):
    curMaxFlow = np.amax(flowData)
    newMaxFlow = curMaxFlow if curMaxFlow > prevMaxFlow else prevMaxFlow
    return newMaxFlow

# Signifier that water is running
def state(finalDataPoint):
    if finalDataPoint == 0:
        waterRunning = 0
    else:
        waterRunning = 1
    return waterRunning

# =================== Data that spans beyond the current session: ===================

# Times that water (or IoT water system) is most commonly used
def usageTimes(histogram, flowTimes): # Pass in an array with all times water is used
    for i in range(len(flowtimes)):
        hourIndex = flowTimes[i].hour - 1
        histogram[hourIndex] += 1
    return histogram

# Total amount of water used over all time
def totalWater(netWaterUsed, waterUsed): # Pass in waterUsed from caller rather than calling function
    netWaterUsed += waterUsed # netWaterUsed from database
    return netWaterUsed

# Average water flow over all time
def meanWater(flowMean, numValues, meanWaterUsed, totalNumValues):
    wavg1 = flowMean * numValues
    wavg2 = meanWaterUsed * totalNumValues
    totalNum = numValues + totalNumValues
    meanWaterUsed = (wavg1 + wavg2)/totalNum # weighted average of flowMean with meanWaterUsed from database
    return meanWaterUsed

# Update metadata in database with new values
def updateMetaData(meanWaterUsed, numValues, totalNumValues, netWaterUsed, histogram, dt):
    db.set_old_avg(meanWaterUsed, dt)
    # store netWaterUsed in database from sql helper function
    totalNumValues += numValues
    # store totalNumValues in database from sql helper function
    # store histogram in database from sql helper function
    return
