print('welcome to E-store')
name_of_customer = input('Enter customer name: ')
number_of_item = int(input('Enter number of items puchased: '))
percentage_discount = int(input('Enter the perentage discount: '))

i = 1

total_of_cost = 0
while i <= number_of_item:	
	each_cost = int(input("Enter cost of items: " ))
	total_of_cost = total_of_cost + each_cost 
	i = i +1
        
print(f'customer name: {name_of_customer} \nnumber of item bought : {number_of_item} \npercentage discount: {percentage_discount} \nOriginal cost: {total_of_cost}')
cost = total_of_cost * percentage_discount / 100
new_cost = total_of_cost - cost

if total_of_cost > 200:
	print(f'\ndiscounted cost : {new_cost}\nthanks for your patronage!')
else:
	print("\ndiscounted cost : 0 (no discount added)\nthanks for your patronage!")