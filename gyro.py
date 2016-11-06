# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MMA8452Q
# This code is designed to work with the MMA8452Q_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Accelorometer?sku=MMA8452Q_I2CS#tabs-0-product_tabset-2

import smbus
import time

bus = smbus.SMBus(1)
global xAcclCal
xAcclCal = 0
yAcclCal = 0
zAcclCal = 0
# Get I2C bus


def calibrate():


	for i in range(0, 10):
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
		global xAcclCal
		xAcclCal += (data[1] * 256 | data[2]) / 16
		
		
		global yAcclCal
		yAcclCal += (data[3] * 256 | data[4]) / 16

		global zAcclCal
		zAcclCal += (data[5] * 256 | data[6]) /16


		xAcclCal = xAcclCal / 10
		yAcclCal = yAcclCal / 10
		zAcclCal = zAcclCal / 10

calibrateTrue = raw_input("Calibrated? (y): ")
while (calibrateTrue is not "y"):
	calibrateTrue = raw_input("Calibrated? (y): ")
	calibrate()
calibrate()
while (True):

	for i in range(0, 10):
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
		xAccl = (data[1] * 256 | data[2]) / 16 - xAcclCal
		yAccl = (data[3] * 256 | data[4]) / 16 - yAcclCal

		zAccl = (data[5] * 256 | data[6]) / 16 - zAcclCal

		xAccl = xAccl / 10
		yAccl = yAccl / 10
		zAccl = zAccl / 10

	cx = (float(xAccl) / float(1<<11) * float(8)) * 22.5
	cy = (float(yAccl) / float(1<<11) * float(8)) * 22.5
	cz = (float(zAccl) / float(1<<11) * float(8)) * 22.5
		
		# Output data to screen
	print "Acceleration in X-Axis : %4f" %cx
	print "Acceleration in Y-Axis : %4f" %cy
	print "Acceleration in Z-Axis : %4f" %cz
