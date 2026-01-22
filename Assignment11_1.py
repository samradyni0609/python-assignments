def ChkPrime(No):
    
    if No<=1:
        print("Not a Prime Number")
        return
    
    for i in range(2,No):
        
        if No%i==0:
            print("Not a Prime Number")
            
    print("Prime Number")
    
A = int(input("Enter the Number:"))

ChkPrime(A)
    
            