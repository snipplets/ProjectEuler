#Observe the following integer sequence generated by picking some small d's

# d = 17	95
# d = 16	79
# d = 15	71
# d = 14	63
# d = 13	57
# d = 12	45
# d = 11	41
# d = 10	31
# d = 9 	27
# d = 8 	21
# d = 7 	17
# d = 6 	11
# d = 5 	9
# d = 4 	5
# d = 3 	3 
# d = 2 	1

#Plugging this into OEIS gives us that this is the sum of phi(i), the sum of the totient functions

limit = 1000001 #due to range ending at the term before the limit
phi = range(limit)

#Sieve style calculation of phi(n) on the fly,
for n in range(2,limit):
	if phi[n] == n: #These are the primes
		for k in range(n, limit, n):
			phi[k] *= 1.0*(n-1)/n

print int(sum(phi))-1 

