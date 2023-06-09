'''a= [[1, 4, 8],
    [2,4,7],
    [1,5,3],]
c=len(a)
x=0
y=0
for i in range(c):
    x+=a[i][i]
    y+=a[i][c-1-i]
    #absolute 
print(abs(x-y)) '''


m= [[12, 4, 18, 11], 
     [133, 23, 10, 21],
     [33, 46, 27, 43],
     [34, 29, 71, 54]]

s=len(m)
for i in range(s):
    for j in range(s//2):
        a= m[i][j], m[i][s-i-1]
print(a)