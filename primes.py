import sys, math

def get_primes(start, n):
	primes = [2]
	next_prime = 3

	while len(primes) < n:
		sqrt = math.sqrt(next_prime)
		i = 0
		flag = True
		while primes[i] <= sqrt:
			if next_prime%primes[i] == 0:
				flag = False
				break
			if i>=len(primes):
				break
			i += 1

		if flag:
			#print next_prime
			primes.append(next_prime)
		next_prime += 2

	return primes
start = int(sys.argv[1])
n = int(sys.argv[2])
comma = ','
print comma.join(map(str,get_primes(start,n)))
