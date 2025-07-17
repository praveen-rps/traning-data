def sumOfdigits(n):
    sum=0
    rem=0
    while n>0:
        rem = n%10
        sum = sum + rem
        n = n//10
    return sum


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(sumOfdigits(n))