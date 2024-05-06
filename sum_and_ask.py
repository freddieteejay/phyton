
user_input = 1
while True:
 first_number = int(input("Enter first number"))
 second_number = int(input("Enter second number"))

 sum = first_number + second_number

 print(f"The sum of {first_number} and {second_number} is {sum}")

 user_input = input("Would you love to perform this operation again ? (yes / no) : ")
 
 if user_input != "yes":
		break