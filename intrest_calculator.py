amount = int(input("Enter amount : "))
number_of_years = int(input("Enter number of years : "))
INTREST_RATE = 20/100


for number in range (number_of_years):
	first_amount = amount * INTREST_RATE
	
	amount  += first_amount
	print(f"The intrest rate of  Year {number + 1} is {amount:,.2f}")