import sql_helpers as db
import dataAnalysis as dA
#import graphing_methods
import datetime as dt


# duration is in seconds
def update_values(duration):
	now = dt.datetime.now()
	times, flowData = db.get_range((now - dt.timedelta(seconds = duration)).strftime('%Y-%m-%d %H:%M:%S.%f'), now)
	FREQ = 1000
	
	# ============ Testing of session-scope functions: ============
	flowMean = dA.meanFlowRate(db.get_avg(), flowData, len(flowData))
	print("Your mean flow rate is", flowMean, "Liters per minute")
	prevFlowMean = flowMean

	waterUsed = dA.totalWaterUsed(db.get_total(), flowData, FREQ)
	print("You have used", waterUsed, "Liters of water")
	prevWaterUsed = waterUsed

	flowMax = dA.maxFlow(db.get_max(), flowData)
	print("The maximum flow rate you reached is", flowMax, "Liters per minute")
	prevMaxFlow = flowMax

	waterRunning = dA.state(flowData[len(flowData) - 1])
	if waterRunning:
		print("The water is running!")
	else:
		print("The water is not running")
	
	# ============ Testing of lifetime-scope functions: ============
	netWaterUsed = dA.totalWater(db.get_total(), waterUsed)
	print("Since installing this system, you have used", netWaterUsed, "Liters of water")

	meanWaterUsed = dA.meanWater(flowMean, len(flowData), db.get_avg(), db.get_num_values())
	print("The average water flow rate for all time is", meanWaterUsed, "Liters per minute")


update_values(1000000000)
