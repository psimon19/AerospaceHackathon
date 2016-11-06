# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MMA8452Q
# This code is designed to work with the MMA8452Q_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Accelorometer?sku=MMA8452Q_I2CS#tabs-0-product_tabset-2

import smbus
import time

bus = smbus.SMBus(1)
xAcclCal = 0
yAcclCal = 0
zAcclCal = 0
# Get I2C bus


def calibrate():


	# MMA8452Q address, 0x1C(28)
	# Select Control register, 0x2A(42)
	#		0x00(00)	StandBy mode
	bus.write_byte_data(0x1D, 0x2A, 0x00)

	# MMA8452Q address, 0x1C(28)
	# Select Control register, 0x2A(42)
	#		0x01(01)	Active mode
	bus.write_byte_data(0x1D, 0x2A, 0x01)

	# MMA8452Q address, 0x1C(28)
	# Select Configuration register, 0x0E(14)
	#		0x00(00)	Set range to +/- 2g
	bus.write_byte_data(0x1D, 0x0E, 0x00)

	time.sleep(0.1)

	# MMA8452Q address, 0x1C(28)
	# Read data back from 0x00(0), 7 bytes
	# Status register, X-Axis MSB, X-Axis LSB, Y-Axis MSB, Y-Axis LSB, Z-Axis MSB, Z-Axis LSB
	data = bus.read_i2c_block_data(0x1D, 0x00, 7)

	#except IOError:
	#	subprocess.call(['i2cdetect', '-y', '1'])
	#	flag = 1

	# Convert the data
	xAcclCal = (data[0] + data[1])
	if xAcclCal > 2047 :
		xAcclCal -= 4096
	
	yAcclCal = (data[2] * 256 + data[3])
	if yAcclCal > 2047 :
		yAcclCal -= 4096

	zAcclCal = (data[4] * 256 + data[5])
	if zAccl > 2047 :
		zAcclCal -= 4096


calibrateTrue = input("Calibrated? (y): ")
	while (calibrateTrue != "y") {
		calibrateTrue = input("Calibrated? (y): ")
	}
calibrate()

while (True):

	
	# MMA8452Q address, 0x1C(28)
	# Select Control register, 0x2A(42)
	#		0x00(00)	StandBy mode
	bus.write_byte_data(0x1D, 0x2A, 0x00)

	# MMA8452Q address, 0x1C(28)
	# Select Control register, 0x2A(42)
	#		0x01(01)	Active mode
	bus.write_byte_data(0x1D, 0x2A, 0x01)

	# MMA8452Q address, 0x1C(28)
	# Select Configuration register, 0x0E(14)
	#		0x00(00)	Set range to +/- 2g
	bus.write_byte_data(0x1D, 0x0E, 0x00)

	time.sleep(0.1)

	# MMA8452Q address, 0x1C(28)
	# Read data back from 0x00(0), 7 bytes
	# Status register, X-Axis MSB, X-Axis LSB, Y-Axis MSB, Y-Axis LSB, Z-Axis MSB, Z-Axis LSB
	data = bus.read_i2c_block_data(0x1D, 0x00, 7)

	#except IOError:
	#	subprocess.call(['i2cdetect', '-y', '1'])
	#	flag = 1

	# Convert the data
	xAccl = (data[0] + data[1]) - xAcclCal
	if xAccl > 2047 :
		xAccl -= 4096
	
	yAccl = (data[2] * 256 + data[3]) - yAcclCal
	if yAccl > 2047 :
		yAccl -= 4096

	zAccl = (data[4] * 256 + data[5]) - zAcclCal
	if zAccl > 2047 :
		zAccl -= 4096

	
	# Output data to screen
	print "Acceleration in X-Axis : %d" %xAccl
#	print "Acceleration in Y-Axis : %d" %yAccl
#	print "Acceleration in Z-Axis : %d" %zAccl