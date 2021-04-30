''' Unfortunately, I procrastinated on this and haven't done much work on it since last week, but everything is working except for a few things:
    The average time used stuff isn't done because there are two ways we could implement it that I wanted to ask you about @Justin
    There are some new metaData values I would like to add to the database, which shouldn't be hard, and the program is already structured for them
    Database updating function is not done, but also should be easy to finish '''

import numpy
import matplotlib.pyplot as plt
import time
import sql_helpers as db
from scipy import stats
from datetime import datetime, timedelta

''' For each new graph frame generated, calculate the following data '''

''' Variables passed into functions from caller: '''
# flowData = flow data points from database since start of session
# numValues = number of values since the start of session - i.e. number of elements in flowData array: numValues = len(flowData)

# prevFlowMean = previous flow mean value for session still stored in looping caller function
# prevWaterUsed = prevous water used value for session still stored in looping caller function
# prevMaxFlow = previous max flow value for session still stored in looping caller function
# finalDataPoint = final point in flow data array, flowData[len(flowData) - 1]

# timesUsed = time array with all times water is used from db
# netWaterUsed = total amount of water used from db metadata
# meanWaterUsed = total number of values in db from db metadata

# Running average flow rate
def meanFlowRate(prevFlowMean, flowData, numValues): 
    flowMean = numpy.mean(flowData + prevFlowMean * numValues)/2
    print("The average flow rate for the session is", flowMean)
    return flowMean

''' For total water used, add current result to result from previous frame. '''
# Total water used throughout session - integral of flow rate over time
def totalWaterUsed(prevWaterUsed, flowData):
    waterUsed = numpy.trapz(flowData) + prevWaterUsed
    print("You used", waterUsed, "Liters of water")
    return waterUsed

# Maximum flow rate attained throughout session
def maxFlow(prevMaxFlow, flowData):
    curMaxFlow = numpy.amax(flowData)
    newMaxFlow = curMaxFlow if curMaxFlow > prevMaxFlow else prevMaxFlow
    return newMaxFlow

''' Keeping temperature functions in for now - keep if we have temperature sensor working later '''

# Average temperature
#def meanTemp(prevTempMean, tempData, numValues):
#    tempMean = (numpy.mean(tempData) + prevTempMean * numValues)/2
#    print(tempMean)
#    return tempMean

''' For range, retreive previous max and min values and compare with current values. 
    Store new max and min values from new values + previous max and min for next frame use '''
# Range of water temperatures
#def rangeTemp(prevMaxTemp, prevMinTemp, tempData):
#    maxComp = [prevMaxTemp, numpy.amax(tempData)]
#    minComp = [prevMinTemp, numpy.amain(tempData)]
#    tempRange = numpy.amax(maxComp) - numpy.amin(minComp)
#    print(tempRange)

# Signifier that water is running
def state(finalDataPoint):
    # Need to initialize waterRunning?
    if finalDataPoint == 0:
        waterRunning = 0
    else:
        waterRunning = 1
    return waterRunning

# Data that spans beyond the current session - Only calculate when desired, or always calculate? Or perhaps at the end of each session

# Times that water (or IoT water system) is most commonly used
def usageTimes(timesUsed): # Pass in an array with all times water is used
    histogram = 0 * [48]
    for i in range(len(timesUsed)):
        hourIndex = timesUsed[i]
        histogram[hourIndex] += 1
    return

# @Justin if we wanted to, this histogram array could be another piece of metadata that's stored in the database - this would make the calculation faster
# We would then only update the histogram for the new time data from the current session, and we would have separate functions for updating hist and finding max    

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
def updateMetaData(meanWaterUsed, numValues, totalNumValues, netWaterUsed):
    # store meanWaterUsed in database
    # store netWaterUsed in database
    totalNumValues += numValues
    # store totalNumValues in databse
    return

# Average water temperature over all time
# do something similar to the other running averages, but multiply the pre-existing average by a much larger number of values
#  def meanTemp():
#    netTempMean = # weighted average of tempMean with netTempMean from database

# Comparison of water usage metrics in some sort of visual display, i.e. plot average temperature for each time the system is used?
# send values back to plotting program ?
# do if we have time