n = int(input())

"""
range(5) 0,1,2,3,4
range(1,5+1) 1,2,3,4,5
range(5,0,-1) 5,4,3,2,1
"""
for i in range(1,n):
    for j in range(n-i):
        print(end=" ")
    
    for k in range(i):
        print(end="* ")
    print()


for i in range(n):
    for j in range(i):
        print(end=" ")
    
    for k in range(n-i):
        print(end="* ")
    print()
# n=int(input("enter the number"))
# for i in range(n):
#     for j in range(n):
#         if(i==j or i+j==n-1 or i==0 or j==0 or i==4 or j==0):
#             print("*",end="")
#         else:
#             print(" ",end=" ")
#     print()
