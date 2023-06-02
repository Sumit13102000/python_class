n=int(input())

def find_size(n):
    count = 0
    while(n!=0):
        n=n//10
        count += 1
        return count
    
def is_armstrong(n):
    size = find_size(n)
    sum = 0
    temp = n
    while(n!=0):
        sum += (n%10)**size
        n = n//10
    if sum==temp:
        return True
    else:
        return False
def arm(n):
    for i in range(n):
        print(f'(i) is armstrong')
    print(size(n))
print(armstrong(i))