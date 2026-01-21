def Factorial(No):
    
    fact = 1
    
    for i in range(1, No+1):
        fact = fact*i
    print(fact)

A = int(input("Enter number: "))
Factorial(A)
