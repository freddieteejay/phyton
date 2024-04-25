
while True:
	gallon_used  =  float(input("Enter the gallons used (-1 to end) : "))	
	if gallon_used == -1:
		break

	elif gallon_used != -1:
		miles_driven = float(input("Enter the miles driven : "))
		print(f"The miles per gallons for this tank was : {miles_driven / gallon_used}")