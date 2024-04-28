def string_counter (word):
	return len(str(word))
	

def first_and_last (word):
	output = ''
	if  len(word) > 2:
		output = word[:2] + word[-2:] 
	if len(word) == 2:
			output = word + word
	if len(word) < 2:
			output = ' '
	return output

def largest_number(number1, number2, number3):
	largest = number1
	if number2 > largest:
		largest = number2
	if number3 > largest:
		largest = number3
	return largest

def smallest_number(number1, number2, number3):
	smallest = number1
	if number2 < smallest:
		smallest = number2
	if number3 < smallest:
		smallest = number3
	return smallest


def minimum(number):
	minimum_num = number[0]
	for num in number:
		if num < minimum_num:
			minimum_num = num
	return minimum_num
	
def maximum(number):
	maximum_num = number[0]
	for num  in number:
		if num > maximum_num:
			maximum_num = num
	return maximum_num

def square_lists(num):
	return ([n ** 2 for n in num])

def sum_num(number):
	return sum([n ** 2 for n in number])

def repeated_word(word,num):
	return word * num

def odd_string(word):
	output= ''
	for i in range(len(word)):
		if i % 2 == 1: 
			output+=word[i]
	return output

def add_ing(word):
	output = ''
	if word[-3:] == "ing":
		output = word + "ly"
	if word[-3:] != "ing":
		output = word + "ing"
	if len(word) == 2:
		output = word
	return output


def long_word(words):
	longest_word = ''
	length = 0
	for word in words:
		if len(word) > length:
			longest_word = word
			length = len(word)
	return longest_word, length				





	
	
	




