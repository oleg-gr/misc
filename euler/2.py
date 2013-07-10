def main():
	fibonachi = (0, 1)
	sum = 0
	even_counter = 1

	while fibonachi[0] + fibonachi[1] < 400000:
		first = fibonachi[0] + fibonachi[1]
		second = first + fibonachi[1]
		fibonachi = (first, second)
		sum += (fibonachi[even_counter] if even_counter != 2 else 0)
		even_counter = (even_counter + 1) % 3

	print(sum)

main()