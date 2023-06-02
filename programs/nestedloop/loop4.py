""""""
n=int(input("Enter the number"))
l=n-1
for i in range (n):
    for j in range(l):
        print(end=" ")
    for k in range(i+1):
        print("'", end=" ")
    print()
    l-=1
     