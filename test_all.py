from roasted_corn import first_and_last,string_counter,largest_number,smallest_number,minimum,maximum,square_lists,sum_num,repeated_word,odd_string,add_ing,long_word


def test_first_and_last():
	assert first_and_last ("semicolon") == "seon"
	assert first_and_last ("on") == "onon"
	assert first_and_last ("o") == " "
	assert first_and_last("sk") == "sksk"



def test_length():
	
	assert string_counter ("semicolon") == 9
	assert string_counter ("fareed") == 6
	assert string_counter ("freddie") == 7
	assert string_counter ("sk") == 2
	assert string_counter ("chi") == 3
	
	

def test_largest():
	assert largest_number (4, 6, 8) == 8
	assert largest_number (2.5, 3.7, 5) == 5
	assert largest_number (-1, -2, -4) == -1
	assert largest_number (10000, 1000, 22222) == 22222


	
	

def test_smallest():
	assert smallest_number (2, 6, 8) == 2
	assert smallest_number (2.5, 3.7, 7.5) == 2.5
	assert smallest_number (-1, -2, -4) == -4

def test_minimum():
	assert minimum ([2, 3, 4, 5, 7]) == 2
	assert minimum ([2.4, 5.7, 4.8, 7.8]) == 2.4
	assert minimum ([-1, -7, -67, -7]) == -67
	assert minimum ([2.4, -56, 6, 0]) == -56


def  test_maximum():
	assert maximum([6, 3, 2, 5, 7]) == 7
	assert maximum ([2.4, 5.7, 4.8, 7.8]) == 7.8
	assert maximum ([-1, -7, -67, -7]) == -1
	assert maximum ([2.4, -56, 6, 0]) == 6

	
def  test_square (): 
	assert square_lists([2, 3, 4, 5, 7]) == [4, 9, 16, 25, 49]
	assert square_lists([-2, -4, -5, -6, -8]) == [4, 16, 25, 36, 64]
	#assert square_lists([ 4.7, 5.3, 8.6, 3.8]) == [22.09, 28.09, 73.96, 14.44]

	
def test_sum ():
	assert sum_num([2, 3, 4, 5, 7]) == 103

def test_repeat ():
	assert repeated_word("hello", 3) == "hellohellohello"

def test_odd ():
	assert odd_string("semicolon") == "eioo"
	assert odd_string("fareed") == "aed"
	assert odd_string("pluto") == 'lt'

def test_add_ly():
	assert add_ing("abc") == "abcing"
	assert add_ing("string") == "stringly"
	assert add_ing("sk") == "sk"
	
	
def test_long_length():
	assert long_word (["welcome", 'out', 'weather', 'mobile', 'breakfast', 'journey']) == ('breakfast', 9)
	assert long_word (["far", "baby", "smart"]) == ("smart", 5)
	
	





