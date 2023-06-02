n = int(input())
isprime = True
 for i in range(2,int(n/2)):
     if n % i == 0:
        isprime = False
        break
     
if isprime:
   print(f"{n}, is a prime number")
else:
   print(f"{n}, is not a prime number")
     
 
    