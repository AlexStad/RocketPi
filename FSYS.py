#FSYS - Alexander St.
#This Flight System has the following purpose:
#Supplying pressure, accelaration and heading data from Enviro pHAT to a text file.

from envirophat import motion, weather
from datetime import datetime


while True:
	t = open('FlightRecord','a')
	t.write("\n " + str(datetime.now().time()))
	t.write("\n " + str(weather.pressure()))
	t.write("\n " + str(weather.altitude()))
	t.write("\n " + str(motion.accelerometer()))
	t.write("\n " + str(motion.heading()))
	t.write("\n ")
	
	t.close()
