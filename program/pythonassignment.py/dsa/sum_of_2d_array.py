a = [(1,2,3), (4,5,6), (7,8,9)]
def sum_of_2darray(a,i,j):
sum = 0
for i in range(len(a)):
    for j in range (len(a[i])):
        sum = sum + a[i][j]
    print(sum)
print()

print(sum)
