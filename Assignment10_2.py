def SumNatural(No):
    
    sum = 0
    
    for i in range(1, No + 1):
        sum = sum+i
    print(sum)

A = int(input("Enter number:"))
SumNatural(A)
