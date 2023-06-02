a = [1,2,3,4,5,6]
b = 1
a.append(None)
for i in range (len(a)-1,0,-1):
    a[i]=a[i-1]
    print(len(a))