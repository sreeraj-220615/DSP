rows=5
ch=ord('A')
for i in range(rows,0,-1):
    for j in range(i):
     print(chr(ch),end="")
    ch+=1
    print()
    