def is_prime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

def main():

	counter = 0
	n = 2

	while counter < 10001:
		if is_prime(n):
			counter += 1
		n += 1
	
	print (n-1, counter)
	
main()