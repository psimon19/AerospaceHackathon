import time
import RPi.GPIO as GPIO
import math

f = open("/var/www/html/log.txt", "w")

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
TPI = 28.0			#Thread per inch
REV = 1			#Revolution
SPR = 3200		#Steps per revolution
ARCCORRECTION = 0.0	#Correction for arc


#dThetaMu 		#Change in theta for 1 micro step
dThetaR	= 0.0 		#Change in theta for 1 revolution

dlRod = 1.0/TPI		#Change in length of the rod (inch)
#dlRodMu				#Change in length of rod per step (inch)

lArms = 8.5
			#Length of arms (inch)
seconds	= 0.0		#Seconds between change

totalTheta = 0.0


#Time in seconds between
def sleepTime():
	global dThetaR
	dThetaR = math.acos(1 - ((dlRod ** 2) / ((2) * (lArms ** 2)))) / SPR
	#dlRodMu = (dlRod) * (1 / SPR)
	#dThetaMu = math.acos(1 - (dlRodMu ** 2) / ((2) * (lArms ** 2)))
	#print dThetaR
	seconds = (dThetaR + ARCCORRECTION) / SIDRATE
	return seconds / 2

def resetBEDPins():
	GPIO.output(stp, GPIO.LOW)
	GPIO.output(dir, GPIO.LOW)
	GPIO.output(MS1, GPIO.LOW)
	GPIO.output(MS2, GPIO.LOW)
	GPIO.output(MS3, GPIO.LOW)
	GPIO.output(EN, GPIO.HIGH)

sleepTime = sleepTime()

def smallStepMode():
	global totalTheta, dThetaR
	GPIO.output(dir, GPIO.LOW)
	GPIO.output(MS1, GPIO.HIGH)
	GPIO.output(MS2, GPIO.HIGH)
	GPIO.output(MS3, GPIO.HIGH)
	for i in range(0, 200):
		GPIO.output(stp, GPIO.HIGH)
		time.sleep(sleepTime)
		GPIO.output(stp, GPIO.LOW)
		time.sleep(sleepTime)
	totalTheta += dThetaR

i = 0;
while (True):
	GPIO.output(EN, GPIO.LOW)
	smallStepMode()
	if (i % 2 == 0):
		f.write("Mount is at {} radians\n\r".format(totalTheta))
		f.flush()
		f.seek(0)
	i+=1

resetBEDPins()
GPIO.cleanup()
