import sql_helpers as db

# TESTER CODE

# ---------------------------------------------------------------------------------------
# get_range_tuple_list(time_start, time_end)

entries = db.get_range_tuple_list('2021-03-19 04:00:00', '2021-03-19 04:00:00')
print(type(entries)) # list
for entry in entries:
	print(entry)

entries = db.get_range_tuple_list('2021-03-19 04:00:00', '2021-03-19 06:00:00')
print(type(entries)) # list
for entry in entries:
	print(entry)

# ---------------------------------------------------------------------------------------
# get_range_into_dataframe(time_start, time_end)

df = db.get_range_into_dataframe('2021-03-19 04:00:00', '2021-03-19 04:00:00')
print(df.head())

df = db.get_range_into_dataframe('2021-03-19 04:00:00', '2021-03-19 06:00:00')
print(df.head())

# ---------------------------------------------------------------------------------------
# get_range(time_start, time_end)

times, flows = db.get_range('2021-03-19 04:00:00', '2021-03-19 04:00:00')
print(type(times)) # list
for time in times:
	print(time)
print(type(flows)) # list
for flow in flows:
	print(flow)

times, flows = db.get_range('2021-03-19 04:00:00', '2021-03-19 06:00:00')
print(type(times)) # list
for time in times:
	print(time)
print(type(flows)) # list
for flow in flows:
	print(flow)
