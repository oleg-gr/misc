def is_prime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	elif not n & 1:
		return False
	else:
		for i in range(3, int(n**0.5) + 1, 2):
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