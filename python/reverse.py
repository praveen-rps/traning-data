n = int(input("enter the number"))
rev = 0
rem = 0

while n>0:
    rem = n%10
    rev = rev*10 + rem
    n = n//10
print("The revers of the numeber is ", rev)