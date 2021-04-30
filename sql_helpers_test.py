import sql_helpers as db
from matplotlib import pyplot as plt

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

# ---------------------------------------------------------------------------------------
# insert_flow(flow, timestamp)

#db.insert_flow(4, "2021-04-09 19:40:27")
#db.insert_flow(5, "2021-04-09 19:40:27.683818")

times, flows = db.get_range('2021-04-15 04:00:00', '2021-04-17 04:00:00')
#plt.scatter(times, flows)
#plt.show()
#plt.savefig('test.png')

print(db.get_old_avg())
db.set_old_avg(10, '2021-04-16 18:41:44.952130')
print(db.get_old_avg())


print(db.get_hist_index(0))
db.set_hist_index(0, 10)
print(db.get_hist_index(0))

db.close_db()



