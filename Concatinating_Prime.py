primes,aq,aw,aa = [],[],[],[]

n=int(input(''))         #taking number upto which u have to find primes
for prime in range(2, n):
    for b in range(2, prime):
        if (prime % b == 0):
            break
    else:
        primes.append(prime)  #found all prime numbers upto N

for a in primes:              #concatinating the primes
     for b in primes[::-1]:
          aq.append(str(a)+str(b)) 

for b in aq:                  
     aw.append(int(b))

for prime in aw:              #finding primes in concatinated primes
    for b in range(2, prime):
        if (prime % b == 0):
            break
    else:
        aa.append(prime)


print (len(aa))
