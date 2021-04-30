# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create a differential ADC channel between Pin 0 and Pin 1
chan = AnalogIn(mcp, MCP.P0, MCP.P1)


# ----------------------------------------------------------------------

from time import sleep
import datetime as dt
import sql_helpers as sql

def calc_flow_rate(period):
	FLOWMETER_SPECIFICATION = 11;
	return 1 / period / FLOWMETER_SPECIFICATION # in L / min

falling = 0
time = 0
TIMESTEP = 0.002
MARGIN_OF_ERROR = 0.01
TIMEOUT = 0.2

prev_state = 0

flow_rates = []

try:
	while(True):
		sleep(TIMESTEP)
		time += TIMESTEP
		#print(chan.voltage)
		
		if(time - falling > TIMEOUT): # if no flow
			falling = time
			if(len(flow_rates) >= 2):
				if(flow_rates[-2][0] == 0 and flow_rates[-1][0] == 0):
					# if no water has been flowing
					flow_rates.pop()
			flow_rates.append((0, dt.datetime.now()))
			sql.insert_flow(0, dt.datetime.now())


		if(chan.voltage < MARGIN_OF_ERROR):
			if(prev_state == 1):
				prev_state = 0
				flow = calc_flow_rate(time - falling)
				flow_rates.append((flow, dt.datetime.now()))
				sql.insert_flow(flow, dt.datetime.now())
				#print(str(flow) + " " + str(time - falling) + " " + str(chan.voltage))
				falling = time
				
		else:
			if(prev_state == 0):
				prev_state = 1;
except:
	print(flow_rates)



