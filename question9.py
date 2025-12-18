n=int(input("Enter n:"))
sum_digits=0
rem=0
while n>0:
    rem=n%10
    sum_digits=sum_digits+rem
    n=n//10
print("Sum of digits:",sum_digits)
