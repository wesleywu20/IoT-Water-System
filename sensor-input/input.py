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


def calc_flow_rate(period):
	FLOWMETER_SPECIFICATION = 11;
	return 1 / period / FLOWMETER_SPECIFICATION # in L / min

falling = 0
time = 0
TIMESTEP = 5
MARGIN_OF_ERROR = 0.01

prev_state = 1

flow_rates = []

try:
	while(True):
		sleep(TIMESTEP)
		time += TIMESTEP
		
		if(chan.value < MARGIN_OF_ERROR):
			if(prev_state == 1):
				prev_state = 0
				
				# only append if flow occurs
				if(time - falling < 200):
					flow_rates.append(calc_flow_rate(time - falling))
				falling = time
				
		else:
			if(prev_state == 0):
				prev_state = 1;
except:
	print(flow_rates)


