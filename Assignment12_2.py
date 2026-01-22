def Factors(No):
    
    for i in range(1,No+1):
        
        if No % i == 0:
            print(i, end=" ")

A = int(input("Enter number:"))
Factors(A)
