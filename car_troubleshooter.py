# Car Troubleshoot

print ""
print "Welcome to the Car Troubleshooter"
print ""
print "Respond to questions with 'y' or 'n'."
print ""


def car_troubleshoot():
	state = True
	while state == True:
		D1 = raw_input("Is the car silent when you turn the key? ")

		if D1 == 'y':
			D1_1 = raw_input("Are the battery terminals corroded? ")
			if D1_1 == 'y':
				print "Clean terminals and try starting again."
				print ""
			if D1_1 == 'n':
				print "Replace cables and try again."
				print ""
				
		if D1 == 'n':
			D1_2 = raw_input("Does the car make a clicking noise? ")
			if D1_2 == 'y':
				print "Replace the battery."
				print ""
			if D1_2 == 'n':
				D2 = raw_input("Does the car crank up but fail to start? ")
				if D2 == 'y':
					print "Check spark plug connections."
					print ""
				if D2 == 'n':
					D3 = raw_input("Does the engine start and then die? ")
					if D3 == 'y':
						D4 = raw_input("Does your car have fuel injection? ")
						if D4 == 'y':
							print "Get it in for service."
							print ""
						if D4 == 'n':
							print "Check to ensure the choke is opening and closing."
							print ""
					if D3 == 'n':
						print "Unsupported."
						print ""

car_troubleshoot()
