number1 = int(input("'Enter an integer: '"))
number2 = int(input('Enter second integer: '))
number3 = int(input("Enter third integer: "))
number4 = int(input('Enter fourth integer: '))
number5 = int(input('Enter fifth integer: '))
             
maximum = number1

if number2  > maximum:
   maximum = number2

if number3 > maximum:
   maximum = number3

if number4 > maximum:
   maximum = number4

if number5 > maximum:
   maximum = number5

minimum = number1

if number2  < minimum:
   minimum = number2

if number3 > maximum:
   minimum = number3

if number4 > maximum:
   minimum = number4

if number5 > maximum:
   minimum = number5

print('minimum value is', minimum)

print('maximum value is',  maximum)

range = maximum - minimum
print('the range is', range)