def is_divisible(n):
	for i in range(1, 21):
		if n % i != 0:
			return False
	return True

def main():
	n = 1
	found = False

	while not found:
		if (is_divisible(n)):
			found = True
			print(n)
		n += 1


main()