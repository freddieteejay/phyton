positive_count = 0
negative_count = 0
zero_count = 0

while True:

 num = int(input("How  many number u wan enter "))
 if num   >  0:
	     	positive_count += 1 

 elif num  <  0:
		negative_count += 1 

 else:
		zero_count += 1

 if num == 0:
        	break 



print(f"\nThe number of positive is: {positive_count}")
print(f"\nThe number of negative is: {negative_count}")
print(f"\nThe total zeros entered is: {zero_count}")


