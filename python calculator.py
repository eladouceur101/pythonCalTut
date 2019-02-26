# Calculator program

#functions for basic calculations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

#division remainder
def divide2(x, y):
    return x % y

#LCM without GCD
def LCM(x, y):
    #choose the greater number
    if x > y:
        greater = x
    else:
        greater = y
        
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
           
    return lcm

#The above is slower and unefficent without using the GCD
# Num1 * Num2 = LCD * GCM
#defint GCD function
def GCD(x, y):
    while(y):
        x, y = y , x % y
    return x

#L.C.M. method using the G.D.C. method
def LCM2(x, y):
    lcm2 = (x*y)//GCD(x,y)
    return lcm2

#method to find all prime numbers between to other numbers
def prime(x, y):
    for pnum in range(x, y + 1):
    # prime numbers are greater than 1
        if pnum > 1:
            for i in range(2, pnum):
                if (pnum % i) == 0:
                    break
        else:
            print(pnum)

#show to cli
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. L.C.M.")
print("6. L.C.M. using G.C.D.")
print("7. All prime numbers between")

#take in inputs
choice = input("Enter operation(1/2/3/4/5/6/7):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#preform action based on users inputted choice

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
    #print(num1, "/", num2, "=", int(divide(num1, num2)), "with a remander of ", divide2(num1, num2))
elif choice == "5":
    print("The L.C.M. of", num1, "and", num2, "is", LCM(num1, num2))
elif choice == "6":
    print("The L.C.M. of", num1, "and", num2, "is", LCM2(num1, num2))
elif choice == "7":
    print("Prime numbers between", num1, "and", num2, "are:")
    print(prime(num1, num2))
#if user inputs a number for choice that we have not assigned
else:
    print("Invalid input for choice.")