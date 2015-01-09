def sum_of_squares(n):
	sum = 0
	for i in range(1, n+1):
		sum = sum + (i*i)
	return sum
	
def square_of_sum(n):
	sum = 0
	for i in range(1, n+1):
		sum = sum + i
	return (sum * sum)
	
def difference(n):
	return square_of_sum(n) - sum_of_squares(n)
		
print difference(100)
