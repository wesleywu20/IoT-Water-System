import numpy
import matplotlib.pyplot as plt
import time

''' This code is not finished - this is just a skeleton/pseudocode for integrating with other parts of the program '''
''' Each piece of the code could be implemented as a function and called by a different program that outputs the data in a visual format '''

# sample data
timeData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
flowData = [30, 32, 33, 34, 34, 37, 41, 46, 43, 48, 49, 50, 50, 51, 56, 57, 56, 63, 78, 67]
tempData = [40, 50, 60, 50, 40, 60, 34, 65, 64, 34, 56, 46, 75, 54]

''' For each new graph frame generated, calculate the following data '''
''' For averages, use the average from the previous frame weighted by the number of values in one frame. '''

# Running average flow rate
flowMean = numpy.mean(flowData) + prev_flow_mean * number_of_values_per_frame)/2
print("The average flow rate for the session is", flowMean)

'''  For total water used, add current result to result from previous frame. '''
# Total water used throughout session - integral of flow rate over time
waterUsed = numpy.trapz(flowData) + prev_water_used
print("You used", waterUsed, "Liters of water")

# Average temperature
tempMean = (numpy.mean(tempData) + prev_temp_mean * number_of_values_per_frame)/2
print(tempMean)

'''For range, retreive previous max and min values and compare with current values. 
   Store new max and min values from new values + previous max and min for next frame use'''
# Range of water temperatures
maxComp = [prev_max_value, numpy.amax(tempData)]
minComp = [prev_min_value, numpy.amain(tempData)]
tempRange = numpy.amax(maxComp) - numpy.amin(minComp)
print(tempRange)

# Signifier that water is running
if final_data_point(s) == 0
    water_not_running
else
    water_running

''' Data that spans beyond the current session '''
    ''' Only calculate when desired, or always calculate? Or perhaps at the end of each session '''

# Times that water (or IoT water system) is most commonly used
''' For this function, perhaps we could do approximate times or time ranges, and print the mode or the top few times '''

# Total amount of water used over all time
netWaterUsed = waterUsed + netWaterUsed from database

# Average water temperature over all time
''' do something similar to the other running averages, but multiply the pre-existing average by a much larger number of values '''
netTempMean = (tempMean + netTempMean * totalTimeClocked)/2

# Comparison of water usage metrics in some sort of visual display, i.e. plot average temperature for each time the system is used?
''' send values back to plotting program ? '''
