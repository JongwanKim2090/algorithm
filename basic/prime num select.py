import math

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def is_prime_eff(x):
    ''' compared to is_prime, is_prime_eff is more efficient in the point of complexity O(x^{1/2})'''
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def eratos(n):
    array = [True for i in range(n+1)]
    arr_prime = []
    for i in range(2, int(math.sqrt(n))+1):
        if array[i] == True:
            j=2
            while i*j <= n:
                array[i*j] = False
                j+=1
    for i in range(2, n+1):
        if array[i]:
            arr_prime.append(i)
    return arr_prime

print(eratos(30))