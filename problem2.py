def gen_fib(seq, limit):
	# Generates a fibonacci sequence whose last term does not exceed the specified limit
	while seq[-1]+seq[-2] < limit:
		seq.append(seq[-1]+seq[-2])
	return seq
	
def get_even_from_fib(fib):
	even_fib = []
	for n in fib:
		if n % 2 == 0: # if n is even
			even_fib.append(n)
	return even_fib
	
def get_sub_from_seq(seq):
	sum = 0
	for n in seq:
		sum = sum + n
	return sum
	
print get_sub_from_seq(get_even_from_fib(gen_fib([1, 2], 4000000)))
