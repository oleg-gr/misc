def get_palindrome():
	for i in range(999,99,-1):
		num = int(str(i) + str(i)[::-1])
		print num
		for j in range(999,499,-1):
			if  num % j == 0 and num / j < 1000:
				return num


def main():
	
	print get_palindrome()

main()