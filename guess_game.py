import random
print("Welcome to guess game")
print("=================== ")
 
LUCKY_NUMBER = random.randrange(1, 10)

user_input = int(input("Enter number : "))
if user_input == LUCKY_NUMBER:
		print("At last u don get am")
else :
		print("You are not correct")

while user_input != LUCKY_NUMBER:
	user_input = int(input("Enter number : "))
	if user_input == LUCKY_NUMBER:
		print("At last u don get am ")
		break
	else:
		print('you are not correct')