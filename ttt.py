grade = int(input('Enter score'))
if grade > 100:
	print('na criminal you be')
elif grade >= 80 and grade <= 100:
   print(f'Congratulations! your grade of {grade} earns you an A in this course')
elif grade >= 65 and grade <= 79:
   print(f'Congratulations! your grade of {grade} earns you an B in this course')
elif grade >= 50 and grade <= 64:
   print(f'Congratulations! your grade of { grade} earns you an C in this course')
elif grade >= 40 and grade <= 49:
   print(f'Congratulations! your grade of {grade} earns you an D in this course')
else:
	print(f'Omo F no dey tire you your score na {grade}' )