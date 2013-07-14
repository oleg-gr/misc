def generate_primes(lim):
   primes = [True] * lim 
   primes[0] = primes[1] = False

   for (i, is_prime) in enumerate(primes):
      if is_prime:
         yield i
         for j in range(i**2, lim, i):
            primes[j] = False

def main():
   print(sum(generate_primes(2000000)))


main()
