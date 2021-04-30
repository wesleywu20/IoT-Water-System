import sql_helpers
import dataAnalysis
import graphing_methods
import datetime as dt


# duration is in seconds
def update_values(duration):
	now = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
	flows, times = sql_helpers.get_range(now - dt.timedelta(seconds = duration), now)
	
	