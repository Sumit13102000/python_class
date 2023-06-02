n=int(input("Enter a number"))
def fibo(n):
    fibo1=0
    fibo2=1
    print(fibo1)
    print(fibo2)
    i=1
    while(i<=n):
        fibo=fibo1+fibo2
        fibo1=fibo2
        fibo2=fibo
        i+=1
        print(fibo)