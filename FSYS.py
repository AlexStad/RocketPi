# FSYS - Alexander St.
# This Flight System has the following purpose:

# Supplying pressure, accelaration and heading data from Enviro pHAT to a file

from envirophat import motion, weather
from datetime import datetime

t = open('FlightRecord', 'a')

while True:
    t.write("\n " + str(datetime.now().time()))
    t.write("\n " + str(weather.pressure()))
    t.write("\n " + str(weather.altitude()))
    t.write("\n " + str(motion.accelerometer()))
    t.write("\n " + str(motion.heading()))
    t.write("\n ")
    t.close()
