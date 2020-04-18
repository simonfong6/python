import sys
import os
import time
import numpy as np

print("Welcome to GPA Calculator!")

def gpaCalc():
	print("Enter typical amount of units per class: ")
	units = float(input())
	print("Enter graded units you have taken so far: ")
	totalUnits = float(input())
	print("Enter current GPA: ")
	currentGPA = float(input())
	#print("Enter goal GPA: ")
	#goalGPA = float(input())

	A = 0
	Aminus = 0
	Bplus = 0

	#for goalGPA in np.arange(3,4,0.1):
##		while (currentGPA < goalGPA and A < 48):
##			currentGPA = (currentGPA * totalUnits+ units * 4) / (totalUnits + units)
##			A+= 1
##			totalUnits += units
##		if (A < 48):
##			print("In order to get a %.3f, you need A's in your next %d %d unit classes!" %(goalGPA, A, units))
##		else:
##			print("You cannot get a GPA of %.3f" % (goalGPA))
	for goalGPA in range(3, 4, 0.1):
		while(currentGPA < goalGPA and A < 48):
			currentGPA = (currentGPA * totalUnits + units * 4) / (totalUnits + units)
			A += 1
			totalUnits += units

		if(A < 48):
                        print("In order to get a %.3f,you need A's in your next %d %d unit classes!" %(goalGPA, A, units))
                else:
                        print("You cannot get a GPA of %.3f" %(goalGPA))



	done = int(input("Do you need anything else? [1/0]: "))
	if(done != 0):
		gpaCalc()
	else:
		print("Thank You!")
	
	return;
	
gpaCalc()

