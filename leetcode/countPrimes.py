#Given an integer n, return the number of prime numbers 
#that are strictly less than n.

def countPrimes(n):
    if(n < 2):
        return 0
    #Creates a List ranged 0 to n
    isPrime = [True] * n
    isPrime[0] = False
    isPrime[1] = False

    for item in range(2, int(math.ceil(math.sqrt(n)))):
        if(isPrime[i]):
            #Every multiple of the i, under i*i, skipping by i (as nothing in between would be a multiple)
            for multiple in range(i*i,n,i):
                isPrime[multiple] = False