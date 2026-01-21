def ChkDivisible(No):
    
    if No%3 == 0 and No%5==0:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")
        
        
A = int(input("Enter Number:"))


ChkDivisible(A)