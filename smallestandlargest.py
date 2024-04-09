number_one = int(input('Enter first integer'))
number_two = int(input("Enter second integer"))
number_three = int(input("Enter third integer"))


sum = number_one + number_two + number_three
average = sum / 3
product = number_one * number_two * number_three
largest = max(number_one,number_two,number_three)
smallest = min(number_one,number_two,number_three)

print(f"The sum  is {sum} \nThe average is{average}\nThe product is{product}\nThe largest number is {largest}\nThe smallest number is {smallest}")