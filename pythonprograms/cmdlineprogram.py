import sys
import ast
def greeting(name):
    print("Hello ",name, "Welcome to Python")

def maths(a,b):
    print("The sum is ",(a+b))
    print("The product is ",(a*b))
    print("The quotient is ",(a//b))
    print("The remainder is ",(a%b))
    print("The difference  is " ,(a-b))


if __name__ == "__main__":
    try:
        if len(sys.argv) < 4:
            print("Invalid number of arguments")
        else:
            greeting(sys.argv[1])
            maths(int(sys.argv[2]), int(sys.argv[3]))
            data = ast.literal_eval(sys.argv[4])
            for i in data:
                print(i)
    except Exception as e:
        print("The exception caught is : ", e)