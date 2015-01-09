array = []
sum = 0

for n in range (1, 1000):
	if n % 3 == 0 or n % 5 == 0:
		array.append(n)
		
for element in array:
	sum = sum + element
	
print sum

# find the sum of all the multiples of 3 or 5 below 1000
