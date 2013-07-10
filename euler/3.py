def find_prime_factors(n):
	i = 2

	while i**2 < n:
		while n % i == 0 and n > i:
			n /= i
		i += 1

	return n

def main():
	print(find_prime_factors(600851475143))

main()