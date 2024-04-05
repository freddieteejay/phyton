
total_score_of_students = 0
for score in range(10):	
	scores = int(input('Enter your scores of students: '))
	
	total_score_of_students += scores 
print(f'average is {total_score_of_students / 10}')