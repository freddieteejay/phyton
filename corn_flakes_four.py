passes = 0 
failes = 0
for student in range (1,16):
		score = int(input("Enter score"))
		

		if score >= 45:
			passes = passes + 1

		else:
			failes = failes + 1
print("passed : ", passes)
print("failed : ", failes)

 