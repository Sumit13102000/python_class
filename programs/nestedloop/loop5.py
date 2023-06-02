n=int(input("enter a number"))
for i in range(n):
    for j in range(n):
      #print(f"{i},{j}",end=" ")
      if i==j or i+j==n-1:
        print("*",end="")
      else:
        print(" ",end="")
    print()



   