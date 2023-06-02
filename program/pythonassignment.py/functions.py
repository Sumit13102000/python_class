n=int(input("Enter a number: "))
def find_size(n):
     count=0
     while(n!=0):
         n=n//10
         count+=1
     return count

def is_armstrong(n):
     size=find_size(n)
     sum=0
     temp=n
     while(n!=0):
         sum +=(n%10)**size
         n=n//10
     if sum==temp:
         return True
     else:
         return False

def armstrong_in_range(n):
     for i in range(1, n+1):
          if is_armstrong(i):
            print (f"{i} is an armstrong number")
          else:
             print (f"{i} is not an armstrong number")

     armstrong_in_range(n)
