import sys
def reverse_number(n):
    rev = 0
    rem = 0
    while n>0:
        rem = n%10
        rev = rev*10 + rem
        n = n//10
    return rev

if __name__ == "__main__":
   #x = int(input("Enter a number: "))
    print(reverse_number(int(sys.argv[1])))
