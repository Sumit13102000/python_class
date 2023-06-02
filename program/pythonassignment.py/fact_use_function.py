n=int(input("Enter a number"))
def fact(n):
    i=1
    fac=1
    while(i<=n):
        fac=fac*i
        i+=1
    return fac
def print_fact(n):
    print(f"Factorial of number {n} is {fact(n)}")

print_fact(n)