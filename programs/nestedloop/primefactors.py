from prime_number import is_prime

def prime_factors(n):

    for i in range(1,n+1):
        if n % i == 0 & is_prime(i):
            print(i, end=" ")

n = int(input())
prime_factors(n)            


