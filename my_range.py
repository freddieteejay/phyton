def ranges(number):
	minimum_num = number[0]
	for num in number:
		if num < minimum_num:
			minimum_num = num
	maximum_num = number[0]
	for num  in number:
		if num > maximum_num:
			maximum_num = num
	return maximum_num - minimum_num
