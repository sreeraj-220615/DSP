C= 50
H=30
values = input("Enter comma separated numbers: ")
arr=[]
for i in values.split(','):
    D =int(i)
    Q = ((2 * C * D)/H) ** (1/2)
    arr.append(str(int(Q)))
result =','.join(arr)
print(result)