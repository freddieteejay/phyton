principal = int(input("Enter the principal amount"))
annualrate  = 7 / 100
number_of_years = int(input('Enter the duration in years'))
base = 1 + annualrate
total = base ** number_of_years
amount = principal * total
print('The amount of deposit is', amount)
