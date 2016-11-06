import math
#Variables 
SIDRATE = .0000727	#Sidereal rate
TPI = 16.0			#Thread per inch
REV = 1.0/16 * TPI	#Revolution
SPR = 3200			#Steps per revolution
ARCCORRECTION = 0 	#Correction for arc

#dThetaMu = 0 		#Change in theta for 1 micro step
dThetaR = 0 		#Change in theta for 1 revolution


dlRod = 1.0/16		#Change in length of the rod (inch)
dlRodMu	= 0			#Change in length of rod per step (inch)

lArms = 8.5			#Length of arms (inch)
seconds	= 0.0		#Seconds between change

debugVar = 0		#debug variable

#Time in seconds between 
def sleepTime():
	dThetaR = math.acos(1 - ((dlRod ** 2) / ((2) * (lArms ** 2)))) / 3200
	#dlRodMu = (dlRod) * (1 / SPR)
	#dThetaMu = math.acos(1 - ((dlRodMu ** 2) / ((2) * (lArms ** 2))))
	print dThetaR / SIDRATE
	print SIDRATE
	seconds = (dThetaR + ARCCORRECTION) / SIDRATE
	return seconds

print sleepTime()