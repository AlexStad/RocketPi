# -*- coding: cp1252 -*-

# Altitude Converter - Alexander Stadelmann
# This Converter has the following purpose:

# Convert Altitude and Time Data from a text file to
# Acceleration and Speed Data and save in a text file

# Create two text files in the directory of this script called:
# "Alti.txt" and "Time.txt", containing one dataset per line.

D = input("How many data sets? ")
St = open("Alti.txt", "r")
Ti = open("Time.txt", "r")
Ac = open("Acceleration.txt", "a")
Sp = open("Speed.txt", "a")
S = St.readlines()
T = Ti.readlines()
n = 1
counter = 1

while n < D:
    n += 1

    AltDif = float(S[n]) - float(S[n-1])
    if AltDif == 0.0:
        Ac.write("\n")
        Sp.write("\n")
        counter += 1
        continue
    TimDif = float(T[n]) - float(T[n-counter])
    Spe = float(AltDif) / float(TimDif)
    Sp.write("\n" + str(Spe))
    AltDif = float(2) * float(AltDif)
    TimDif = float(TimDif) * float(TimDif)
    Acc = float(AltDif) / float(TimDif)
    Acc = float(Acc) / float(9.81)
    Acc += 1
    Ac.write("\n" + str(Acc))
    counter = 1

St.close()
Ti.close()
Ac.close()
Sp.close()
