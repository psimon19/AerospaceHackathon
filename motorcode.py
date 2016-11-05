import time
import RPi.GPIO as GPIO

EN = 7
MS1 = 11
MS2 = 13
MS3 = 15
stp = 16
dir = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(EN, GPIO.OUT)
GPIO.setup(MS1, GPIO.OUT)
GPIO.setup(MS2, GPIO.OUT)
GPIO.setup(MS3, GPIO.OUT)
GPIO.setup(stp, GPIO.OUT)
GPIO.setup(dir, GPIO.OUT)

count = 0

#Variables
SIDRATE = .0000727	#Sidereal rate
TPI = 16			#Thread per inch
REV = 1/16 * TPI	#Revolution
SPR = 3200			#Steps per revolution
ARCCORRECTION = 0 	#Correction for arc

dThetaMu = 		#Change in theta for 1 mu step
#ThetaR	 = 		#Change in theta for 1 revolution


dlRod = 1/16		#Change in length of the rod
dlRodMu				#Change in length of rod per step
lArms = 			#Length of arms
seconds				#Seconds between change

#Time in seconds between 
def sleepTime():
	#dThetaR = math.acos((dlRod ** 2) / ((2) * (lArms ** 2)))
	dlRodMu = (dlRod) * (1 / SPR)
	dThetaMu = math.acos((dlRodMu ** 2) / ((2) * (lArms ** 2)))
	seconds = (dThetaMu + ARCCORRECTION) / SIDRATE
	return seconds

def resetBEDPins():
	GPIO.output(stp, GPIO.LOW)
	GPIO.output(dir, GPIO.LOW)
	GPIO.output(MS1, GPIO.LOW)
	GPIO.output(MS2, GPIO.LOW)
	GPIO.output(MS3, GPIO.LOW)
	GPIO.output(EN, GPIO.HIGH)

def smallStepMode():
	GPIO.output(dir, GPIO.LOW)
	GPIO.output(MS1, GPIO.HIGH)
	GPIO.output(MS2, GPIO.HIGH)
	GPIO.output(MS3, GPIO.HIGH)
	for i in range(0, 200):
		GPIO.output(stp, GPIO.HIGH)
		time.sleep(0.02)
		GPIO.output(stp, GPIO.LOW)
		time.sleep(0.02)

GPIO.output(EN, GPIO.LOW)
smallStepMode()
resetBEDPins()

GPIO.cleanup()
