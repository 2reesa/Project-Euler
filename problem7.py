# By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def def_prime(x):
	n = x
	arr = []
	for n in range(x, 0, -1):
		if x % n == 0: # if n is a factor of x
			arr.append(n)
			if len(arr) > 2:
				return 0
	if len(arr) < 3:
		return 1

def gen_primes(limit):
	x = 2
	count = 0
	last_prime = 0
	while count < limit:
		if def_prime(x) == 1:
			count = count + 1
			print count, "of", limit, "processed, ", limit-count, "remaining (", (count/(limit*1.00))*100, "%)"
			last_prime = x
		x = x + 1
	return last_prime
	
#print gen_primes(6)	
print gen_primes(10001)
