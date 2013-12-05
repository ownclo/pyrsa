from random import getrandbits

# n - number of bits to generate
def genRand(n):
    return getrandbits(n)

def isPrime(number):
    return True

def genPrime(n):
    rand = genRand(n)
    if isPrime(rand):
        return rand
    else: return -1

    #while not isPrime(rand):
        #rand = genRand(n)
    #return rand

n = input("Enter key length: ")
print genPrime(n)
