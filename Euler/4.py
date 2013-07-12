def get_palindrome(n):
	upperlim = int ("9" * n)
	lowerlim = int ("9" * (n - 1))
	uppercheck = 1 + int("9" * n) #to check if second product is n-digit long
	for i in range(upperlim, lowerlim, -1):
		num = int(str(i) + str(i)[::-1])
		for j in range(upperlim, 1, -1): 
			if  num % j == 0 and num / j < uppercheck:
				return num


def main():
	
	print(get_palindrome(3)) #number of digits in multipliers

main()