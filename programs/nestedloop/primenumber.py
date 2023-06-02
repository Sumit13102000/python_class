def is_prime(n):
    for i in range(1, n/2):
     if n%i==0:
       return False
    return True
    